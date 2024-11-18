# This code snippet sets up a Streamlit web application using LangChain and the OpenAI API to create a chatbot or assistant interface. It lets users ask questions and receive responses directly from OpenAI's language model, specifically `gpt-3.5-turbo`.

# Here’s a breakdown of the code:

# ### Step-by-Step Explanation

# 1. **Environment Setup**:
#    - **Environment Variables**: It uses the `dotenv` library to load environment variables from a `.env` file, specifically `OPENAI_API_KEY` and `LANGCHAIN_API_KEY`.
#    - **Setting Environment Variables**: These keys are then set into the environment, which allows LangChain and OpenAI to authenticate requests.

# 2. **Prompt Template**:
#    - **Creating a Prompt Template**: Using LangChain’s `ChatPromptTemplate`, it builds a simple template where the assistant is told to be helpful, and it is structured to take user questions as inputs.
#    - This template helps structure the interaction between the user and the assistant. 

# 3. **Streamlit Framework**:
#    - **User Interface**: Streamlit is used to create a basic web interface.
#    - **User Input**: The `st.text_input` function allows users to enter a question or topic.
#    - **Response Display**: When the user enters a query, `st.write` displays the assistant's response.

# 4. **LangChain Pipeline**:
#    - **LLM (Language Model)**: The code initializes `ChatOpenAI` with the specified model (`gpt-3.5-turbo`), connecting the LangChain pipeline to OpenAI's model.
#    - **Output Parser**: `StrOutputParser` processes the raw output of the language model into a string for easier display.
#    - **Chain Creation**: The `|` syntax in LangChain allows for chaining components—here, `prompt | llm | output_parser` forms a complete query-response pipeline.
#    - **Response Generation**: `chain.invoke` is called with the user's input, generating the assistant’s response.

# ### Purpose and How It Works

# This setup is used to quickly deploy a web-based chatbot where:
# - **Streamlit** manages the frontend, allowing users to input questions and see responses in real-time.
# - **LangChain** handles the query pipeline and template, providing an organized way to manage prompts, model calls, and output parsing.
# - **OpenAI API** enables the underlying language model, powering the assistant’s responses.

# When a user types in a question:
# 1. **Input Processing**: The question goes through the prompt template, which structures it for the model.
# 2. **Response Generation**: The model (via OpenAI API) generates a response.
# 3. **Output Parsing and Display**: The response is parsed and displayed on the Streamlit interface.

# This code is useful for creating demos or prototypes where natural language processing capabilities are needed, especially in scenarios involving interactive Q&A or assistant-like features.
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
    
    
    # streamlit run chatbot/app.py
 