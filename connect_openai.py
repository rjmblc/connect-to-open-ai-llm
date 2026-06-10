import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# load env variables to env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#print(OPENAI_API_KEY)

# initialize model
def connect_openai():
    llm = ChatOpenAI(
        model = "gpt-3.5-turbo",
        temperature= 0,        
    )

    return llm

# ask llm
def fire_prompt(llm):
    response = llm.invoke("What is the capital of India")
    print(response.content)


if __name__ == "__main__":
    llm = connect_openai()
    fire_prompt(llm = llm)

