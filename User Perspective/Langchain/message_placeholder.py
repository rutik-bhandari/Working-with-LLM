# Problem Statement : 
# Demonstrate how to use MessagesPlaceholder inside a ChatPromptTemplate to insert previous conversation history
# dynamically into the prompt.

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder   #Used to dynamically insert previous chat history into the
# prompt at runtime.

chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    #Placeholder where previous conversation history will be inserted dynamically.
    # variable_name specifies the key that will receive the chat history while invoking the template.
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

with open('User Perspective/Langchain/chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

prompt = chat_template.invoke({'chat_history':chat_history,'query': 'where is my refund?'})

print(prompt)