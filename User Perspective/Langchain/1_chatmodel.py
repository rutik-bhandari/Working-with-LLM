#Problem Statement : Connect to a Hugging Face chat model using LangChain, and asks a question, and prints the AI's response.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint  
# HuggingFaceEndpoint : its task is to connect to a model hosted on Hugging Face.
# ChatHuggingFace converts that model into a LangChain Chat Model, which allows to use Langchain features

from dotenv import load_dotenv  # load environment variables

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",  # model name
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)  # Create a LangChain chat model using the Hugging Face endpoint.

result = model.invoke("What is the capital of Australia")   # sends input query to model

print(result.content)
