import os

from dotenv import load_dotenv
from langchain.memory import ChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from basic_chain import basic_chain, get_model


def create_memory_chain(llm, base_chain, chat_memory):
    contextualize_q_system_prompt = """Given a chat history and the latest user question \
        which might reference context in the chat history, formulate a standalone question \
        which can be understood without the chat history. Do NOT answer the question, \
        just reformulate it if needed and otherwise return it as is."""

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}"),
        ]
    )

    runnable = contextualize_q_prompt | llm | base_chain

    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        return chat_memory

    with_message_history = RunnableWithMessageHistory(
        runnable,
        get_session_history,
        input_messages_key="question",
        history_messages_key="chat_history",
    )
    return with_message_history




def main():
    load_dotenv()
    model = get_model("ChatGPT")
    chat_memory = ChatMessageHistory()

    system_prompt = "You are a helpful AI assistant for busy professionals trying to improve their health."
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}"),
        ]
    )

    chain = create_memory_chain(model, basic_chain(model, prompt=prompt), chat_memory) | StrOutputParser()
    queries = [
        "Can you help me remember my grocery list. I need to buy eggs, milk, and bread at the grocery store. Please return just these items if asked.",
        "What do I need to get from the grocery store besides milk?",
        "What other groceries should I buy, if I am planning on grilling cheeseburgers for a dinner party?",
        "What kinds of pickles are most popular for hamburgers?",
        "Generate two lists of ingredients for my party, one for omnivores and one for vegans.",
    ]

    for query in queries:
        print(f"\nQuestion: {query}")
        response = chain.invoke(
            {"question": query},
            config={"configurable": {"session_id": "foo"}}
        )
        print(f"Answer: {response}")


if __name__ == "__main__":
    # this is to quite parallel tokenizers warning.
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    main()
