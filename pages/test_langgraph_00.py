import os
import getpass

from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"Enter {var}: ")

def _get_env(var: str):
    return os.environ.get(var)

openapi_api_key = _get_env("OPENAI_API_KEY")
# _set_env("ANTHROPY_API_KEY")

class State(TypedDict):
    # Messages have the type "list".
    # The "add_messages" function in the annotation defines 
    # how this state key should be updated
    # (in this case, it appends message to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

# from langchain_anthropic import ChatAnthropic
# llm = ChatAnthropic(model_name="claude-3-5-haiku-20241022")

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=openapi_api_key)

def chatbot(state: State):
    return { "messages": [llm.invoke(state["messages"])] }

# the first argument is the unique node name
# the second argument is the function or object that will be called whenever the node is called.
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant: ", value["messages"][-1].content)

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit", "q", "bye"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break
