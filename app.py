import streamlit as st
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor

st.title('My Awesome Agent 🤖')

# --- Agent Setup ---
# 1. Define the Tools
tools = [TavilySearch(max_results=1)]

# 2. Pull the Prompt from the Hub
prompt = hub.pull("hwchase17/react")

# 3. Define the Model
model = ChatOllama(model="llama3")

# 4. Create the Agent
agent = create_react_agent(model, tools, prompt)

# 5. Create the Agent Executor with error handling
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)
# --- End of Agent Setup ---

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if user_input := st.chat_input("Ask a question..."):
    # Add user's message to history and display it
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get and display agent's response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Use the agent_executor's .invoke() method
            response = agent_executor.invoke({"input": user_input})
            st.markdown(response["output"])

    # Add agent's final response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response["output"]})