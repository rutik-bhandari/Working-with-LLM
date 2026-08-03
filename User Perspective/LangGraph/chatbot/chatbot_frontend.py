import streamlit as st
from chatbot_backend import chatbot,retrieve_all_threads
from langchain_core.messages import HumanMessage
# uuid (Universally Unique Identifier) is used to generate random, globally unique IDs. 
# In chatbot/RAG applications, it is commonly used to assign unique IDs to users, documents, sessions, or vector store records.
import uuid

#------------------- Utility Functions -----------------------------------------

def generate_thread_id():
     thread_id = uuid.uuid4()
     return thread_id

def reset_chat():
     thread_id = generate_thread_id()
     st.session_state['thread_id'] = thread_id
     add_thread(st.session_state['thread_id'])
     st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    # Check if messages key exists in state values, return empty list if not
    return state.values.get('messages', [])

#--------------------- Session Setup ------------------------------------------------

# st.session_state is a dictionary-like object used to store data across Streamlit reruns. 
# It helps preserve values (such as chat history) even though the script executes from top to bottom after every user interaction.
# Check whether 'message_history' already exists in Streamlit's session state.
# If not, initialize it as an empty list to store the conversation history.
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
     st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()

add_thread(st.session_state['thread_id'])

#--------------------Sidebar UI-----------------------------------------

st.sidebar.title('LangGraph based Chatbot')

if st.sidebar.button('New Chat'):
     reset_chat()

st.sidebar.header('My Conversation')

# Display all chat threads (latest first) in the sidebar.
# When a thread is selected, load its conversation history.
for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)

        # Convert LangChain message objects into a format
        # suitable for displaying in the Streamlit chat UI.
        temp_messages = []

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_messages.append({'role': role, 'content': msg.content})
        # Update the current chat history displayed in the UI.
        st.session_state['message_history'] = temp_messages


#------------------------------Main UI--------------------------------------------

# Load the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input("Type here")

if user_input:
    st.session_state['message_history'].append({'role':'user','content':user_input})
    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}
    with st.chat_message('user'):
        st.text(user_input)
    with st.chat_message('assistant'):
            ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= CONFIG,
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
