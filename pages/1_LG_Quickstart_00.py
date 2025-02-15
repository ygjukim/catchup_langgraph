import streamlit as st
import streamlit.components.v1 as components
from langgraph_sidebar_content import LG_QuickStart_00_sidebar
from my_modules import view_source_code
import os

st.title('Agentic Workflow PPT')
st.write('')
st.write('For bigger screen, click the link below.')
st.markdown(""" - [Google Slide Src](https://docs.google.com/presentation/d/1vF7TV2zFOjQL1AiPNJFypQagOHYxMG5Hhom-K87DN6E/edit?usp=sharing) """)
st.write('')

# embed streamlit docs in a streamlit app
components.iframe("https://docs.google.com/presentation/d/1vF7TV2zFOjQL1AiPNJFypQagOHYxMG5Hhom-K87DN6E/edit?usp=sharing", height =1000, width = 1500)

current_file_name = os.path.basename(__file__)
view_source_code(current_file_name)

LG_QuickStart_00_sidebar()