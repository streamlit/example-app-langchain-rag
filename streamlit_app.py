import os

import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory

from ensemble import ensemble_retriever_from_docs
from full_chain import create_full_chain, ask_question
from local_loader import load_txt_files

st.set_page_config(page_title="LangChain & Streamlit RAG")
st.title("LangChain & Streamlit RAG")


def show_ui(qa, prompt_to_user="How may I help you?"):
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": prompt_to_user}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User-provided prompt
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = ask_question(qa, prompt)
                st.markdown(response.content)
        message = {"role": "assistant", "content": response.content}
        st.session_state.messages.append(message)


@st.cache_resource
def get_retriever():
    docs = load_txt_files()
    return ensemble_retriever_from_docs(docs)


def get_chain():
    ensemble_retriever = get_retriever()
    chain = create_full_chain(ensemble_retriever, chat_memory=StreamlitChatMessageHistory(key="langchain_messages"))
    return chain


def run():
    ready = True
    if 'HUGGINGFACEHUB_API_TOKEN' in st.secrets:
        st.write("Found HUGGINGFACEHUB_API_TOKEN secret")
        os.environ['HUGGINGFACEHUB_API_TOKEN'] = st.secrets['HUGGINGFACEHUB_API_TOKEN']
    if 'OPENAI_API_KEY' in st.secrets:
        st.write("Found OPENAI_API_KEY secret")
        os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

    if 'HUGGINGFACEHUB_API_TOKEN' not in os.environ:
        st.write("Missing HUGGINGFACEHUB_API_TOKEN")
        ready = False
    if 'OPENAI_API_KEY' not in os.environ:
        st.write("Missing OPENAI_API_KEY")
        ready = False

    # TODO: let them enter their own key if not provided.

    if ready:
        chain = get_chain()
        st.subheader("Ask me questions about this week's meal plan")
        show_ui(chain, "What would you like to know?")


run()
