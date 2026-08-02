# problem statement : Demonstrate how to use ChatPromptTemplate to create a
# reusable chat prompt containing multiple message types
# (System, Human, AI, etc.) with dynamic placeholders.

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'drs system'})

print(prompt)