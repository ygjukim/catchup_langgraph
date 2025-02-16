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

    # Define chatbot node
    def chatbot(state: State):
        return {"messages": [llm.invoke(state["messages"])]}
    
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)

    graph = graph_builder.compile()

    try:
        graph_bytes = graph.get_graph().draw_mermaid_png()

        st.image(graph_bytes, caption="Chatbot Graph")

    except Exception as e:
        st.error(f"Error drawing graph: {e}")

    if "messages_01" not in st.session_state:
        st.session_state.messages_01 = []

    # Display all previous messages
    for messages in st.session_state.messages_01:
        with st.chat_message(messages["role"]):
            st.markdown(messages["content"])

    # Get new user input and process it
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages_01.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Prepare he entire chat history to senf to the model
        full_conversation = [(m["role"], m["content"]) for m in st.session_state.messages_01]
        
        # Generate response using the model with the full conversation history
        for event in graph.stream({"messages": full_conversation}):
            for value in event.values():
                response = value["messages"][-1].content
                st.session_state.messages_01.append({"role": "assistant", "content": response})
                with st.chat_message("assistant"):
                    st.markdown(response)

def main():
    # add button to Sidebar to reset session state
    with st.sidebar:
        if st.button("Reset Session"):
            st.session_state.clear()
            st.rerun()      # Rerun the app to reflect the changes

    st.title('LangGraph Chatbot Super Basic 🏠')

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
            
        if st.button("Submit"):
            if api_key:
                st.session_state.api_key = api_key
                st.session_state.api_key_submitted = True
            else:
                st.error("Please input your LLM API Key.")
    
    if st.session_state.api_key_submitted:
        LangGraph_run()

if __name__ == "__main__":
    main()

current_file_name = os.path.basename(__file__)
view_source_code(current_file_name)

LG_QuickStart_02_sidebar()