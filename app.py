import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase 
from langchain.agents.agent_types import AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

st.set_page_config(page_title="Chat with SQL Database", page_icon="🦜")
st.title("Chat with SQL database")

INJECTION_WARNING = """
    SQL Agent can be vulnerable to prompt injection. Use a DB role with minimal permissions.
"""

LOCALDB = 'USE_LOCALDB'
MYSQL = 'USE_MYSQL'

radio_options = ["Use SQLlite3 Database - Student.db", "Connect to your MySQL database"]

selected_option = st.sidebar.radio(label = "Choose the DB with which you want to chat", options=radio_options)

if radio_options.index(selected_option)==1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input('Provide MySQL host')
    mysql_user = st.sidebar.text_input('Enter user name')
    mysql_password = st.sidebar.text_input('Enter your password', type = 'password')
    mysql_db = st.sidebar.text_input('Enter MySQL Database')
else:
    db_uri = LOCALDB

api_key = st.sidebar.text_input(label='Enter your groq api key', type = 'password')

if not db_uri:
    st.info('Please enter the db information and uri')
    
llm = None
if api_key:
    llm = ChatGroq(
        groq_api_key=api_key, 
        model_name='llama-3.3-70b-versatile', 
        streaming=True
    )

if not llm:
    st.error("Please enter a valid Groq API key to continue.")
    st.stop()
    
## Connecting the database

@st.cache_resource(ttl = '2h')
def configure_db(db_uri, mysql_host = None, mysql_user = None, mysql_password = None, mysql_db = None):
    if db_uri==LOCALDB:
        dbfilepath = (Path(__file__).parent/'student.db').absolute()
        print(dbfilepath)
        creator = lambda: sqlite3.connect(f'file:{dbfilepath}?mode=ro', uri = True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    elif db_uri == MYSQL:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error('Please provide all MySQL connection details')
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))    
        
if db_uri == MYSQL:
    db = configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db = configure_db(db_uri)
    
## Toolkit
if api_key:
    toolkit = SQLDatabaseToolkit(db = db, llm = llm)
    agent = create_sql_agent(
        llm = llm,
        toolkit = toolkit,
        verbose = True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors = True
    )
else:
    st.warning("Enter api key to enable chat with database")

if 'messages' not in st.session_state or st.sidebar.button("Clear chat history"):
    st.session_state['messages'] = [{'role':'assistant', 'content': 'How can I help you?'}]
    
for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])
    
user_query = st.chat_input(placeholder="Ask anything from database")

if user_query:
    st.session_state.messages.append({"role":'user', 'content': user_query})
    st.chat_message('user').write(user_query)
    
    with st.chat_message('assistant'):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[streamlit_callback])
        st.session_state.messages.append({'role':'assistant', 'content':response})
        st.write(response)

