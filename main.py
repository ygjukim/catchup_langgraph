import streamlit as st
import streamlit.components.v1 as components
from langgraph_sidebar_content import main_sidebar

st.set_page_config(
    page_title="Catchup LangGraph Tutorial",
    page_icon="👋",
)

st.write("# Catchup LangGraph Tutorial!👋")

st.write("LangGraph is a framework for building conversational AI applications.")
st.markdown(
    """
    - [LangGraph Website](https://www.langchain.com/langgraph)
"""
)

st.write("Look before you start LangGraph")
st.markdown(
    """
    - [Grhph Theory and LangGraph](https://youtu.be/mvGp8Wz3KdI?si=VJJSx_xaGP2OsTC-)
"""
)

st.markdown(
    """
    # CatchUp AI related materials

    - [Catchup AI Youtube Channel](https://www.youtube.com/@catchupai)
    - [Catchup LangChain Streamlit Web App](https://catchuplangchain.streamlit.app/)
    - [Catchup AI Streamlit Web App](https://catchupai.streamlit.app/)
    - [Catchup AI for Small Business App](https://catchupai4sb.streamlit.app/)
    - [Catchup AI Tistory Blog](https://coronasdk.tistory.com/)
    - [Deep Learning Fundamental PPT (Eng. Ver.)](https://docs.google.com/presentation/d/1F4qxSAv9g13de99rS8fcp4e1LCfrILq8QaahXCPx1Pw/edit?usp=sharing)
    - [Deep Learning Fundamental PPT (Kor. Ver.)](https://docs.google.com/presentation/d/15KNzGnSnJx_4ToSBM2MrHiC2q5MiVe0plOs7f3NJuWM/edit?usp=sharing)
    - [AI Web App Development 101 PPT](https://docs.google.com/presentation/d/18_6z05tmR_loTPWFHj8PCY3-uCNKuoy-IvE0g5ms8YM/edit?usp=sharing)
"""
)

main_sidebar()
