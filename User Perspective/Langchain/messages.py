# Message concept : while building any chatbot, model should know -> who's speaking?, is it user msg? 
# is it system instruction, or is it previous AI response....
# Here comes message concept in langchain

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()


model2 = ChatMistralAI(
    model="mistral-large-2512"
)

messages=[
    SystemMessage(content='You are a comic'),
    HumanMessage(content='Tell me about LangChain')
]

result = model2.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)