# SQL Database Chat Application 🦜

A Streamlit-based application that allows users to interact with SQL databases using natural language queries. The app uses LangChain agents powered by Groq's LLaMA model to translate natural language questions into SQL queries and provide intelligent responses.

## Features

- **Natural Language Queries**: Ask questions about your database in plain English
- **Multiple Database Support**: Connect to SQLite3 or MySQL databases
- **Interactive Chat Interface**: Streamlit-powered chat UI with conversation history
- **Real-time Streaming**: Live response streaming using Groq's API
- **Secure Connection**: Password-protected database connections
- **Sample Database**: Includes a pre-built student database for testing

## Tech Stack

- Frontend: Streamlit
- AI/LLM: Groq API (LLaMA 3.3 70B)
- Agent Framework: LangChain
- Database: SQLite3, MySQL
- ORM: SQLAlchemy
- Language: Python 3.8+

## Prerequisites

Before running the application, ensure you have:

- Python 3.8 or higher
- A Groq API key ([Get one here](https://groq.com/))
- MySQL server (if using MySQL option)

## Installation

1. Clone the repository or download the files:
```bash
git clone https://github.com/keshavv17/SQL-Chat.git
cd SQL-Chat
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501`

### Using the Interface

1. **Choose Database Type**: 
   - Select "Use SQLlite3 Database - Student.db" for the sample database
   - Select "Connect to your MySQL database" for your own MySQL database

2. **Enter API Key**: 
   - Input your Groq API key in the sidebar

3. **MySQL Configuration** (if selected):
   - Enter MySQL host address
   - Provide username and password
   - Specify database name

4. **Start Chatting**:
   - Type natural language questions in the chat input
   - Examples: "Show me all students", "What's the average marks?", "Who scored the highest in Physics?"

## Sample Queries

Try these example queries with the student database:

- "How many students are there in total?"
- "Show me all students in section A"
- "What's the average marks of all students?"
- "Which student has the highest marks?"
- "List all students studying Computer Science"
- "Show me students with marks above 90"
- "What subjects are available in the database?"

## File Structure

```
├── app.py                 # Main Streamlit application
├── sqlite.py      # Script to create sample SQLite database
├── student.db            # SQLite database (created after running setup)
└── README.md             # This file
```

## Dependencies

- `streamlit`: Web application framework
- `langchain-community`: LangChain community packages
- `langchain-groq`: Groq integration for LangChain
- `sqlalchemy`: SQL toolkit and ORM
- `sqlite3`: SQLite database interface (built-in)
- `mysql-connector-python`: MySQL database connector
- `pathlib`: Path manipulation utilities
