# Message concept : while building any chatbot, model should know -> who's speaking?, is it user msg? 
# is it system instruction, or is it previous AI response....
# Here comes message concept in langchain

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct"
)
model = ChatHuggingFace(llm=llm) 

messages=[
    SystemMessage(content='You are a comic'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)