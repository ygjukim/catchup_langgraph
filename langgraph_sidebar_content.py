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

def LG_QuickStart_02_sidebar():
    st.sidebar.header("LangGraph Enhancing the Chatbot with Tool 🧰")
    st.sidebar.markdown(
        """
        Tool : TavilySearchResults, bind_toolst, Python Typing Literal, add_conditional_edge
        \nThis page is an LangGraph example of implementing a Chatbot with Tool.
    """
    )
    st.sidebar.markdown(
        """
        ## Items to study in this example:

        - [LangGraph QuickStart 02](https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-2-enhancing-the-chatbot-with-tools)
        - [Tavily Search](https://python.langchain.com/v0.2/docs/integrations/tools/tavily_search/)
        - [TavilySearchResult API 1](https://python.langchain.com/v0.2/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)
        - [TavilySearchResult API 2](https://api.python.langchain.com/en/latest/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)
        - [Tool Calling - bind tools](https://python.langchain.com/v0.2/docs/how_to/tool_calling/)
        - [Tool Calling Blog](https://blog.langchain.dev/tool-calling-with-langchain/)
        - [LangChain Core messages](https://python.langchain.com/v0.2/api_reference/core/messages.html)
        - [Python Typing Literal](https://docs.python.org/3/library/typing.html)
        - [add_conditional_edge](https://langchain-ai.github.io/langgraph/concepts/low_level/#conditional-edges)
    """
    )
    st.sidebar.markdown(
        """
        ## Youtube Clip

        - [Youtube Clip](https://www.youtube.com/playlist?list=PLRQGNaa1hGF3Xr-IL21Y6w7OKa-8ts7m5)
    """
    )

def LG_QuickStart_03_sidebar():
    st.sidebar.header("LangGraph Adding Memory to the Chatbot 🧰")
    st.sidebar.markdown(
        """
        Tool : LangGraph Memory, Checkpointers, ToolNode, tools_condition, get_state
        \nThis page covers the basics of memory management in LangGraph.
    """
    )
    st.sidebar.markdown(
        """
        ## Items to study in this example:

        - [LangGraph QuickStart 03](https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-3-adding-memory-to-the-chatbot)
        - [CoLab Source](https://colab.research.google.com/drive/1SARxtUTLUpLi4tX0v4E1oIC_xe1nhQa_?usp=sharing)
        - [How to add memory to your graph](https://langchain-ai.github.io/langgraph/how-tos/persistence/)
        - [Checkpointers-MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#memorysaver)
        - [ToolNode](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html)
        - [ToolNode API Reference](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html)
        - [tools_condition](https://langchain-ai.github.io/langgraph/reference/prebuilt/#toolinvocation)
        - [graph.get_state](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/)
    """
    )
    st.sidebar.markdown(
        """
        ## Youtube Clip

        - [Youtube Clip](https://www.youtube.com/playlist?list=PLRQGNaa1hGF12WIRH4Mb0UPMEYMlFT06v)
    """
    )
