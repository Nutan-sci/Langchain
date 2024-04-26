#from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import strOutputParser

import streamlit as st
import os
from dotenv import load_doten

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

## langsmith tracking
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

## prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

##streamlit framework

st.title('Langchain Demo with OPENAI API')
input_text = st.text_input('Search the topic you want')

llm = ChatOpenAI(model="gpt3.5-turbo")
output_parser = strOutputParser()
chain = prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({'qiestion':input_text}))



