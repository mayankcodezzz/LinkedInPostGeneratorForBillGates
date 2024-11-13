from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
load_dotenv()
llm = ChatGroq(groq_api_key = os.getenv("GROQ_API_KEY"), model_name="llama-3.2-90b-text-preview")
if __name__ == "__main__":
    response = llm.invoke("what is the 2 best words to describe about bill gates")
    print(response.content)
