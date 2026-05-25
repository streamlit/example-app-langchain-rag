import os
<<<<<<< HEAD
from dotenv import load_dotenv

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate

from basic_chain import get_model
from ensemble import ensemble_retriever_from_docs
=======

from dotenv import load_dotenv
from langchain.memory import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate

from basic_chain import get_model
from filter import ensemble_retriever_from_docs
>>>>>>> 83d150474fd50d8dae19df2ecf2b57c061bfa497
from local_loader import load_txt_files
from memory import create_memory_chain
from rag_chain import make_rag_chain


<<<<<<< HEAD
def create_full_chain(retriever, groq_api_key=None, chat_memory=ChatMessageHistory()):
    model = get_model(groq_api_key=groq_api_key)

    system_prompt = """You are a helpful AI assistant for busy professionals trying to improve their health.
Use the following context and the users' chat history to help the user.
If you don't know the answer, just say that you don't know.

Context: {context}

Question: """
=======
def create_full_chain(retriever, openai_api_key=None, chat_memory=ChatMessageHistory()):
    model = get_model("ChatGPT", openai_api_key=openai_api_key)
    system_prompt = """You are a helpful AI assistant for busy professionals trying to improve their health.
    Use the following context and the users' chat history to help the user:
    If you don't know the answer, just say that you don't know. 
    
    Context: {context}
    
    Question: """
>>>>>>> 83d150474fd50d8dae19df2ecf2b57c061bfa497

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{question}"),
        ]
    )

    rag_chain = make_rag_chain(model, retriever, rag_prompt=prompt)
    chain = create_memory_chain(model, rag_chain, chat_memory)
    return chain


def ask_question(chain, query):
    response = chain.invoke(
        {"question": query},
<<<<<<< HEAD
        config={"configurable": {"session_id": "foo"}},
=======
        config={"configurable": {"session_id": "foo"}}
>>>>>>> 83d150474fd50d8dae19df2ecf2b57c061bfa497
    )
    return response


def main():
    load_dotenv()
<<<<<<< HEAD
    from rich.console import Console
    from rich.markdown import Markdown

=======

    from rich.console import Console
    from rich.markdown import Markdown
>>>>>>> 83d150474fd50d8dae19df2ecf2b57c061bfa497
    console = Console()

    docs = load_txt_files()
    ensemble_retriever = ensemble_retriever_from_docs(docs)
    chain = create_full_chain(ensemble_retriever)

    queries = [
<<<<<<< HEAD
        "Generate a grocery list for my family meal plan for the next week (following 7 days). "
        "Prefer local, in-season ingredients.",
        "Create a list of estimated calorie counts and grams of carbohydrates for each meal.",
=======
        "Generate a grocery list for my family meal plan for the next week(following 7 days). Prefer local, in-season ingredients."
        "Create a list of estimated calorie counts and grams of carbohydrates for each meal."
>>>>>>> 83d150474fd50d8dae19df2ecf2b57c061bfa497
    ]

    for query in queries:
        response = ask_question(chain, query)
        console.print(Markdown(response.content))


<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == '__main__':
    # this is to quiet parallel tokenizers warning.
>>>>>>> 83d150474fd50d8dae19df2ecf2b57c061bfa497
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    main()
