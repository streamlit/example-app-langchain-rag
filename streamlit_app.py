import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_community.embeddings import HuggingFaceEmbeddings

from ensemble import ensemble_retriever_from_docs
from full_chain import create_full_chain, ask_question
from local_loader import load_txt_files

st.set_page_config(
    page_title="RAG Chatbot · Groq + LangChain",
    page_icon="🤖",
    layout="centered",
)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🤖 RAG Chatbot")
st.caption("Powered by **Groq** · **LangChain** · **Streamlit**")
st.divider()


# ── Chat UI ───────────────────────────────────────────────────────────────────
def show_ui(qa, prompt_to_user="How may I help you?"):
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": prompt_to_user}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question about your documents…"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking…"):
                    try:
                        response = ask_question(qa, prompt)
                        st.markdown(response.content)
                        st.session_state.messages.append(
                            {"role": "assistant", "content": response.content}
                        )
                    except Exception as e:
                        error_msg = f"⚠️ Error generating response: {e}"
                        st.error(error_msg)


# ── Cached retriever (keyed on API key so it rebuilds if key changes) ─────────
@st.cache_resource(show_spinner="Loading documents & building index…")
def get_retriever():
    docs = load_txt_files()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return ensemble_retriever_from_docs(docs, embeddings=embeddings)


def get_chain(groq_api_key):
    retriever = get_retriever()
    chain = create_full_chain(
        retriever,
        groq_api_key=groq_api_key,
        chat_memory=StreamlitChatMessageHistory(key="langchain_messages"),
    )
    return chain


# ── Sidebar ───────────────────────────────────────────────────────────────────
def run():
    with st.sidebar:
        st.header("⚙️ Configuration")

        # Resolve API key: secrets > session > manual input
        groq_api_key = st.session_state.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", "")

        if not groq_api_key:
            st.markdown("### 🔑 Groq API Key")
            groq_api_key = st.text_input(
                "Enter your Groq API key",
                type="password",
                placeholder="gsk_…",
                help="Get a free key at https://console.groq.com",
            )
            if groq_api_key:
                st.session_state["GROQ_API_KEY"] = groq_api_key
            st.markdown("[Get a free Groq API key ↗](https://console.groq.com)", unsafe_allow_html=False)
        else:
            st.success("✅ Groq API key loaded", icon="🔑")

        st.divider()
        st.markdown("### 📂 Documents")
        st.info(
            "Place `.txt`, `.pdf`, or `.md` files in the **`data/`** folder, "
            "then restart the app to reindex them.",
            icon="ℹ️",
        )

        st.divider()
        st.markdown(
            "Built with [LangChain](https://langchain.com) · "
            "[Groq](https://groq.com) · "
            "[Streamlit](https://streamlit.io)"
        )

    if not groq_api_key:
        st.warning("👈 Please enter your **Groq API key** in the sidebar to get started.")
        st.stop()

    try:
        chain = get_chain(groq_api_key)
        st.subheader("💬 Ask me anything about your documents")
        show_ui(chain, "What would you like to know?")
    except Exception as e:
        st.error(f"Failed to initialise the chain: {e}")
        st.stop()


run()
