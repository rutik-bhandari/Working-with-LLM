# What is PromptTemplate?
#
# A PromptTemplate is a reusable prompt with placeholders.
# Instead of writing a new prompt every time, we create a
# template once and insert dynamic values (variables) at runtime.

from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint  
from dotenv import load_dotenv 

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct"
)

model = ChatHuggingFace(llm=llm)

# template:
# The actual prompt text that will be sent to the LLM after
# replacing placeholders with actual values.
#
# input_variables:
# List of placeholder names that must be provided while
# generating the final prompt.
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

prompt = template2.invoke({'name':'Rutik'})

result = model.invoke(prompt)

print(result.content)