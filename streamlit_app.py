import streamlit as st
from langchain.llms import OpenAI

st.title('QuickStart App')

open_api_key = st.sidebar.text_input('Open API Key')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, open_api_key=open_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)    
