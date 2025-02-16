import os
import getpass
import streamlit as st

from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, AIMessage
from langgraph_sidebar_content import LG_QuickStart_02_sidebar
from my_modules import view_source_code, modelName, claudeHaikuModelName

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"Enter {var}: ")

def _get_env(var: str):
    return os.environ.get(var)

# openapi_api_key = _get_env("OPENAI_API_KEY")
# anthropy_api_key = _get_env("ANTHROPY_API_KEY")

def LangGraph_run():
    # Define the state for storing messages
    class State(TypedDict):
        messages: Annotated[list, add_messages]

    graph_builder = StateGraph(State)

    # Define LLM model
    claudeModelName = claudeHaikuModelName()
    chatbotModelName = modelName()

    if st.session_state.model_choice == "Anthropic Claude":
        llm = ChatAnthropic(
            api_key=st.session_state.api_key, 
            model_name=claudeModelName)
    elif st.session_state.model_choice == "OpenAI ChatGPT":
        llm = ChatOpenAI(
            openai_api_key=st.session_state.api_key, 
            model_name=chatbotModelName)

    # Define chatbot node using LLM with tools and add chatbot node to the state graph
    os.environ["TAVILY_API_KEY"] = st.session_state.tavily_api_key
    tool = TavilySearchResults(max_results=2)
    tools = [tool]
    
    llm_with_tool = llm.bind_tools(tools)
    
    def chatbot(state: State):
        # print(f"LLM 호출: {state}")
        return {"messages": [llm_with_tool.invoke(state["messages"])]}
    
    graph_builder.add_node("chatbot", chatbot)

    # Define search node using Tavily search tool and add the node to the state graph
    import json
    from langchain_core.messages import ToolMessage 

    class BasicToolNode:
        """ A node that runs the tools rquested in the last AIMessage."""
        
        def __init__(self, tools: list) -> None:
            self.tools_by_name = {tool.name: tool for tool in tools}
            
        def __call__(self, inputs: dict):
            if messages := inputs.get("messages", []):
                message = messages[-1]
            else:
                raise ValueError("No messages found in inputs")
            
            outputs = []
            for tool_call in message.tool_calls:
                # print(f"Tool 실행: {tool_call}")
                tool_result = self.tools_by_name[tool_call["name"]].invoke(tool_call["args"])
                outputs.append(
                    ToolMessage(
                        content=json.dumps(tool_result),
                        tool=tool_call["name"],
                        tool_input=tool_call["args"],
                        tool_call_id=tool_call["id"],
                    )
                )
            
            # print(f"Tool outputs: {outputs}")
            return {"messages": outputs}

    tool_node = BasicToolNode(tools = tools)
    graph_builder.add_node("tool_node", tool_node)
    
    # Add condiftional edge between chatbot and tool node
    from typing import Literal
    
    def route_tools(state: State) -> Literal["tool_node", "__end__"]:
        """ Use in the conditional edge to route to the tool node if the last message has tool calls.
            Otherwise, route to the end of the graph.
        """
        if isinstance(state, list):
            ai_message = state[-1]
        elif messages := state.get("messages", []):
            ai_message = messages[-1]
        else:
            raise ValueError(f"No messages found in input state to tool_edge: {state}")
       
        if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
            return "tool_node"
        return "__end__"
                
    # The `tools_condition` function returns "tools" if the chatbot asks to use a tool, and "__end__" if
    # it is fine directly responding. This conditional routing defines the main agent loop.
    graph_builder.add_conditional_edges(
        "chatbot",
        route_tools,
        # The following dictionary lets you tell the graph to interpret the condition's outputs as a specific node
        # It defaults to the identity function, but if you
        # want to use a node named something else apart from "tools",
        # You can update the value of the dictionary to something else
        # e.g., "tools": "my_tools"
        {"tool_node": "tool_node", "__end__": "__end__"},
    )

    # Any time a tool is called, we return to the chatbot to decide the next step
    graph_builder.add_edge("tool_node", "chatbot")
    graph_builder.add_edge(START, "chatbot")

    graph = graph_builder.compile()

    # Display the graph
    try:
        graph_bytes = graph.get_graph().draw_mermaid_png()

        st.image(graph_bytes, caption="Chatbot Graph")

    except Exception as e:
        st.error(f"Error drawing graph: {e}")

    # Initialize session state
    if "messages_02" not in st.session_state:
        st.session_state.messages_02 = []

    # Display all previous messages
    for messages in st.session_state.messages_02:
        with st.chat_message(messages["role"]):
            st.markdown(messages["content"])

    # Get new user input and process it
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages_02.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Prepare he entire chat history to senf to the model
        full_conversation = [(m["role"], m["content"]) for m in st.session_state.messages_02]
        
        # Generate response using the model with the full conversation history
        # i = 0
        for event in graph.stream({"messages": full_conversation}):
            for value in event.values():
                # i = i + 1
                # print(f"Values #{i}: {value}")
                
                if isinstance(value["messages"][0], AIMessage):
                    ai_message = value["messages"][0]
                    
                    if not hasattr(ai_message, "tool_calls") or not ai_message.tool_calls:
                        response = ai_message.content
                        st.session_state.messages_02.append({"role": "assistant", "content": response})
                        with st.chat_message("assistant"):
                            st.markdown(response)

def main():
    # add button to Sidebar to reset session state
    with st.sidebar:
        if st.button("Reset Session"):
            st.session_state.clear()
            st.rerun()      # Rerun the app to reflect the changes

    st.title('LangGraph Chatbot with Tools 🏠')

    if "model_choice" not in st.session_state:
        st.session_state.model_choice = "OpenAI ChatGPT"

    model_choice = st.radio("Choose your LLM model", ["OpenAI ChatGPT", "Anthropic Claude"])

    if model_choice != st.session_state.model_choice:
        st.session_state.clear()
        st.session_state.model_choice = model_choice

    if "api_key_submitted" not in st.session_state:
        st.session_state.api_key_submitted = False

    if not st.session_state.api_key_submitted:
        if st.session_state.model_choice == "OpenAI ChatGPT":
            api_key = st.text_input("Please input your OpenAI API Key:", type="password")
        elif st.session_state.model_choice == "Anthropic Claude":
            api_key = st.text_input("Please input your Anthropy API Key:", type="password")

        if "tavily_api_key" not in st.session_state:
            tavily_api_key = st.text_input("Please input your Tavily API Key:", type="password")
                    
        if st.button("Submit"):
            if api_key and tavily_api_key:
                st.session_state.api_key = api_key
                st.session_state.tavily_api_key = tavily_api_key
                st.session_state.api_key_submitted = True
            else:
                st.error("Please input your LLM API Key and Tavily API key.")
                         
    if st.session_state.api_key_submitted:
        LangGraph_run()

if __name__ == "__main__":
    main()

current_file_name = os.path.basename(__file__)
view_source_code(current_file_name)

LG_QuickStart_02_sidebar()