from langchain_openai import ChatOpenAI
import streamlit as st
# from langchain.globals import set_debug

# set_debug(True)

with st.sidebar:
    st.title("Provide Your API Key")
    OPENAI_API_KEY = st.text_input("OpenAI API Key", type="password")

if not OPENAI_API_KEY:
    st.info("Enter Open AI Key to continue")
    st.stop()
llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

st.title("Ask Anything")

question = st.text_input("Enter the question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)