import streamlit as st

def main_sidebar():
    st.sidebar.success("Select a demo above.")

    st.sidebar.markdown(
        """
        - [LangGraph](https://www.langchain.com/langgraph)
        - [LangGraph Overview](https://langchain-ai.github.io/langgraph/)
        - [LangGraph Tutorials](https://langchain-ai.github.io/langgraph/tutorials/)
        - [LangGraph How To Guides](https://langchain-ai.github.io/langgraph/how-tos/)
        - [LangGraph Conceptual Guides](https://langchain-ai.github.io/langgraph/concepts/)
        - [LangGraph API Reference](https://langchain-ai.github.io/langgraph/reference/graphs/)
        - [LangGraph Cloud(beta)](https://langchain-ai.github.io/langgraph/cloud/)
    """
    )

def LG_QuickStart_00_sidebar():
    st.sidebar.header("Agentic Workflow 🏠")
    st.sidebar.markdown(
        """
        Concept : LangGraph, Agent, Agentic Workflow, Multi Agent, LangGraph Studio
        \nThis page is intended to help you understand Agentic Workflow and Multi Agent implemented by LangGraph..
    """
    )
    st.sidebar.markdown(
        """
        ## Links where you can get the references.

        - [What are AI Agents? by IBM Youtube](https://youtu.be/F8NKVhkZZWI?si=zn-ocGpgDSiNw_nR)
        - [Agentic Workflow by Andrew Ng Youtube](https://youtu.be/8b7CLBCS3pg?si=flccfrk0cTGh9e9N)
        - [LangGraph Studio Youtube](https://youtu.be/nhvF5PCRcLM?si=2-xu6hSv2qzz2oSL)
        - [LangChain blog for LangGraph Studio](https://blog.langchain.dev/langgraph-studio-the-first-agent-ide/)
        - [LangGraph Studio GitHub (Download)](https://github.com/langchain-ai/langgraph-studio)
    """)
    st.sidebar.markdown(
        """
        ## Youtube Clip

        - [Youtube Clip](https://www.youtube.com/playlist?list=PLRQGNaa1hGF3MuCgWRkZm0hR7HqzD3y_C)
    """
    )

def LG_QuickStart_01_sidebar():
    st.sidebar.header("LangGraph+Streamlit Chatbot 🧑‍🎨")
    st.sidebar.markdown(
        """
        Tool : Annotated, TypedDict, StateGraph, Anthropic Claude, Nodes, Edges, LangGraph Compile, LangGraph Stream, Streamlit Session State
        \nThis page is an example of implementing a Chatbot with LangGraph, StreamLit, and Claude. You can also learn the basic usage of LangGraph.
    """
    )
    st.sidebar.markdown(
        """
        ## Items to study in this example:

        - [LangGraph QuickStart 01](https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-1-build-a-basic-chatbot)
        - [Python Typing](https://docs.python.org/3/library/typing.html)
        - [Annotated Research Blog](https://medium.com/@life-is-short-so-enjoy-it/research-about-python-typing-annotated-95c9093f97c3)
        - [Python TypedDict](https://peps.python.org/pep-0589/)
        - [mypy TypedDict](https://mypy.readthedocs.io/en/stable/typed_dict.html)
        - [StateGraph, Nodes, Edges, Compile](https://blog.langchain.dev/langgraph/)
        - [Anthropic API key](https://www.anthropic.com/)
        - [LangGraph Stream](https://langchain-ai.github.io/langgraph/reference/graphs/#streammode)
        - [Streamlit Session State](https://youtu.be/qCPbT2YB_E4?si=Pxyuo7WQUcs5D6jl)
    """
    )
    st.sidebar.markdown(
        """
        ## Youtube Clip

        - [Youtube Clip](https://www.youtube.com/playlist?list=PLRQGNaa1hGF32cN2PuSEyvFF6A1TVRKRj)
    """
    )

def LC_QuickStart_02_sidebar():
    st.sidebar.header("LangChain QuickStart 02 🧐")
    st.sidebar.markdown(
        """
        Tools : beautifulsoup4, WebBaseLoader, OpenAIEmbeddings, FAISS, RecursiveCharacterTextSplitter, create_stuff_documents_chain, create_retrieval_chain
        \nRetrieval is useful when you have too much data to pass to the LLM directly. You can then use a retriever to fetch only the most relevant pieces and pass those in.
        \nIn this process, we will look up relevant documents from a Retriever and then pass them into the prompt. A Retriever can be backed by anything - a SQL table, the internet, etc - but in this instance we will populate a vector store and use that as a retriever
    """
    )
    st.sidebar.markdown(
        """
        ## Items to study in this example:

        - [LangChain QuickStart](https://python.langchain.com/v0.1/docs/get_started/quickstart)
        - [Vector stores](https://python.langchain.com/docs/modules/data_connection/vectorstores)
        - [Bueatifulsoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
        - [WebBaseLoader](https://python.langchain.com/docs/integrations/document_loaders/web_base)
        - [WebBaseLoader API](https://api.python.langchain.com/en/latest/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html)
        - [OpenAI Embeddings](https://python.langchain.com/docs/integrations/text_embedding/openai)
        - [FAISS](https://python.langchain.com/docs/integrations/vectorstores/faiss)
        - [FAISS API](https://api.python.langchain.com/en/latest/vectorstores/langchain_community.vectorstores.faiss.FAISS.html)
        - [RecursiveCharacterTextSplitter](https://python.langchain.com/docs/modules/data_connection/document_transformers/recursive_text_splitter)
        - [RecursiveCharacterTextSplitter API](https://api.python.langchain.com/en/latest/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html)
        - [Chains](https://python.langchain.com/docs/modules/chains)
        - [create_stuff_documents_chain API](https://api.python.langchain.com/en/latest/chains/langchain.chains.combine_documents.stuff.create_stuff_documents_chain.html)
        - [create_retrival_chain API](https://api.python.langchain.com/en/latest/chains/langchain.chains.retrieval.create_retrieval_chain.html#)
    """
    )

def LC_QuickStart_02_RemedialClass_sidebar():
    st.sidebar.header("LangChain QuickStart 02 Remedial Class ✍🏻")
    st.sidebar.markdown(
        """
        Tools : RecursiveCharacterTextSplitter() params, as_retriever() prams, VectorStore
        \nIn this page, we will explore the parameters available for use in RecursiveCharacterTextSplitter() and as_retriever().
    """
    )
    st.sidebar.markdown(
        """
        ## Items to study in this example:

        - [Recursively split by character](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/recursive_text_splitter/)
        - [Blog for RecursivelyCharacterTextSplitter](https://dev.to/eteimz/understanding-langchains-recursivecharactertextsplitter-2846)
        - [RecursiveCharacterTextSplitter](https://python.langchain.com/docs/modules/data_connection/document_transformers/recursive_text_splitter)
        - [RecursiveCharacterTextSplitter API](https://api.python.langchain.com/en/latest/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html)
        - [Vector stores](https://python.langchain.com/docs/modules/data_connection/vectorstores)
        - [Vector Store API](https://api.python.langchain.com/en/latest/vectorstores/langchain_core.vectorstores.VectorStore.html)
        - [Vector store backed retriever](https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/vectorstore/)
    """
    )

def LC_QuickStart_03_CoversationRetrievalChain_sidebar():
    st.sidebar.header("LangChain QuickStart 03 🗣️")
    st.sidebar.markdown(
        """
        Tools : create_history_aware_retriever, MessagesPlaceholder, HumanMessage, AIMessage
        \nThe previous chain can only handle single questions, but to accommodate follow-up questions in applications like chat bots, modifications are needed.
        \nTwo adjustments are crucial
        \n1. The retrieval method must consider the entire history, not just the latest input.
        \n2. The final LLM chain should also incorporate the entire history.
    """
    )
    st.sidebar.markdown(
        """
        ## Items to study in this example:

        - [LangChain QuickStart](https://python.langchain.com/v0.1/docs/get_started/quickstart)
        - [create_history_aware_retriever](https://api.python.langchain.com/en/latest/chains/langchain.chains.history_aware_retriever.create_history_aware_retriever.html)
        - [Conversational RAG](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/)
        - [How to add chat history](https://python.langchain.com/v0.2/docs/how_to/qa_chat_history_how_to/)
        - [How to stream results from your RAG application](https://python.langchain.com/v0.2/docs/how_to/qa_streaming/)
        - [Add message history(memory)](https://python.langchain.com/v0.1/docs/expression_language/how_to/message_history/)
        - [ConversationalRetrievalChain API](https://api.python.langchain.com/en/latest/chains/langchain.chains.conversational_retrieval.base.ConversationalRetrievalChain.html)
        - [Types of MessagepromptTemplate](https://python.langchain.com/docs/modules/model_io/prompts/message_prompts)
        - [MessagePlaceholder](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html)
        - [HumanMessage](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.human.HumanMessage.html)
        - [AIMessage](https://api.python.langchain.com/en/v0.0.339/schema/langchain.schema.messages.AIMessage.html)
    """
    )
    st.sidebar.markdown(
        """
        ## Youtube Clip

        - [Youtube Clip](https://youtu.be/EQ6c9309T8c?si=pMUgmF4xMClk3SaI)
    """
    )

def LC_QuickStart_04_Chatbot_sidebar():
    if st.sidebar.button('Reset Session'):
        st.session_state.clear()
        st.rerun(scope='app')

    st.sidebar.header("RAG News Chatbot 📰")
    st.sidebar.markdown(
        """
        Tool : st.session_state, st.chat_message, st.chat_input, RecursiveCharacterTextSplitter
        \nOn this page, we learn how to implement a Chatbot with LangChain's Retriever using Streamlit's session_state and chat_message.
    """
    )
    st.sidebar.markdown(
        """
        ## Items to study in this example:

        - [Streamlit session_state](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state)
        - [Streamlit chat_message](https://docs.streamlit.io/develop/api-reference/chat/st.chat_message)
        - [Streamlit chat_input](https://docs.streamlit.io/develop/api-reference/chat/st.chat_input)
        - [Streamlit chat melements](https://docs.streamlit.io/develop/api-reference/chat)
        - [Advanced concepts of Streamlit](https://docs.streamlit.io/get-started/fundamentals/advanced-concepts)
    """
    )
    st.sidebar.markdown(
        """
        ## Youtube Clip

        - [Youtube Clip](https://www.youtube.com/watch?v=qCPbT2YB_E4)
    """
    )

def LC_QuickStart_05_Agent_sidebar():
    st.sidebar.header("LangChain QuickStart 04 👨‍🔧")
    st.sidebar.markdown(
        """
        Tools : hub, create_openai_functions_agent, AgentExecutor, StreamlitCallbackHandler, get_openai_callback
        \nAgents in LangChain are systems that use a language model to interact with other tools. They can be used for tasks such as grounded question/answering, interacting with APIs, or taking action. LangChain provides: A standard interface for agents.
    """
    )
    st.sidebar.markdown(
        """
        ## Items to study in this example:

        - [LangChain QuickStart](https://python.langchain.com/v0.1/docs/get_started/quickstart)
        - [LangChain Hub](https://docs.smith.langchain.com/cookbook/hub-examples)
        - [LangSmith](https://docs.smith.langchain.com/)
        - [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
        - [Concepts of Agents](https://python.langchain.com/v0.1/docs/modules/agents/concepts/)
        - [create_openai_functions_agent](https://python.langchain.com/docs/modules/agents/agent_types/openai_functions_agent)
        - [create_openai_functions_agent API](https://api.python.langchain.com/en/latest/agents/langchain.agents.openai_functions_agent.base.create_openai_functions_agent.html)
        - [LangChain AgentExcutor API](https://api.python.langchain.com/en/latest/agents/langchain.agents.agent.AgentExecutor.html)
        - [StreamlitCallbackHandler](https://python.langchain.com/v0.2/docs/integrations/callbacks/streamlit/)
        - [StreamlitCallbackHandler API](https://api.python.langchain.com/en/latest/callbacks/langchain_community.callbacks.streamlit.streamlit_callback_handler.StreamlitCallbackHandler.html)
        - [get_openai_callback](https://python.langchain.com/docs/modules/model_io/llms/token_usage_tracking)
        - [get_openai_callback API](https://api.python.langchain.com/en/v0.0.341/callbacks/langchain.callbacks.manager.get_openai_callback.html)
    """
    )
    st.sidebar.markdown(
        """
        ## Youtube Clip

        - [Youtube Clip](https://www.youtube.com/watch?v=Yy0DVD2PlYY)
    """
    )

