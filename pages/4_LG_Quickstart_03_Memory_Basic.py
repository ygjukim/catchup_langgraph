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
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph_sidebar_content import LG_QuickStart_03_sidebar
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
    tool_node = ToolNode(tools=tools)
    graph_builder.add_node("tool_node", tool_node)
    
    # Add condiftional edge between chatbot and tool node
    graph_builder.add_conditional_edges(
        "chatbot", 
        tools_condition, 
        {"tool_node": "tool_node", "__end__": "__end__"}
    )

    # Any time a tool is called, we return to the chatbot to decide the next step
    graph_builder.add_edge("tool_node", "chatbot")
    graph_builder.add_edge(START, "chatbot")

    # Compile the graph with checkpointer to save the state of the chatbot    
    graph = graph_builder.compile(MemorySaver())

    # Display the graph
    try:
        graph_bytes = graph.get_graph().draw_mermaid_png()

        st.image(graph_bytes, caption="Chatbot Graph")

    except Exception as e:
        st.error(f"Error drawing graph: {e}")

    config1 = { "configurable": { "thread_id": "1"}}
    config2 = { "configurable": { "thread_id": "2"}}

    def displayChatMessage(events):
        for event in events:
            if isinstance(event["messages"][-1], AIMessage):
                role = "assistant"
            else:
                role = "user"

            with st.chat_message(role):
                st.markdown(event["messages"][-1].content)

    def stream_graph_update(config, user_input):
        events = graph.stream(
            {"messages": [("user", user_input)]}, 
            config=config,
            stream_mode="values")
        displayChatMessage(events)

    user_input_1_1 = "Hi there! My name is YoungChul."
    user_input_1_2 = "I am in South Korea?"
    user_input_remrmber = "Remember my name?"
    user_input_capital = "What is the capital of the country?"
    user_input_2_1 = "Hi there! My name is Doug."
    user_input_2_2 = "I am in USA."

    # The config is the **second positional argument** to stream() or invoke()!
    st.write(config1)
    stream_graph_update(config1, user_input_1_1)    
    stream_graph_update(config1, user_input_1_2) 
    stream_graph_update(config1, user_input_remrmber)
    st.write(config2)
    stream_graph_update(config2, user_input_remrmber)  
    stream_graph_update(config2, user_input_2_1) 
    stream_graph_update(config2, user_input_2_2) 
    stream_graph_update(config2, user_input_remrmber)   
    stream_graph_update(config2, user_input_capital)
    st.write(config1)
    stream_graph_update(config1, user_input_remrmber)  
    stream_graph_update(config1, user_input_capital) 

    snapshot1 = graph.get_state(config1)
    snapshot2 = graph.get_state(config2)

    with st.expander("Snapshot for config1"):
        st.write(str(snapshot1))

    with st.expander("Snapshot for config2"):
        st.write(str(snapshot2))        

def main():
    # add button to Sidebar to reset session state
    with st.sidebar:
        if st.button("Reset Session"):
            st.session_state.clear()
            st.rerun()      # Rerun the app to reflect the changes

    st.title("LangGraph MemorySaver Basic Tutorial")

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

LG_QuickStart_03_sidebar()