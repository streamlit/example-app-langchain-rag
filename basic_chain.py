import os
from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

DEFAULT_MODEL = "llama-3.1-8b-instant"


def get_model(model_name=DEFAULT_MODEL, groq_api_key=None, **kwargs):
    """Return a ChatGroq model instance."""
    api_key = groq_api_key or os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            "No Groq API key found. Set GROQ_API_KEY in your environment or "
            "pass groq_api_key= when calling get_model()."
        )
    return ChatGroq(
        groq_api_key=api_key,
        model_name=model_name,
        temperature=0,
        **kwargs,
    )


def basic_chain(model=None, prompt=None):
    if model is None:
        model = get_model()
    if prompt is None:
        prompt = ChatPromptTemplate.from_template(
            "Tell me the most noteworthy books by the author {author}"
        )
    return prompt | model


def main():
    load_dotenv()
    prompt = ChatPromptTemplate.from_template(
        "Tell me the most noteworthy books by the author {author}"
    )
    chain = basic_chain(prompt=prompt) | StrOutputParser()
    result = chain.invoke({"author": "William Faulkner"})
    print(result)


if __name__ == "__main__":
    main()
