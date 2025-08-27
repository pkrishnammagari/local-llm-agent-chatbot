import os
# Updated imports for the latest versions
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor

# Make sure your TAVILY_API_KEY is set in your environment
# export TAVILY_API_KEY="your_key_here"

# 1. Define the Tools using the new class name
tools = [TavilySearch(max_results=1)]

# 2. Pull the Prompt
prompt = hub.pull("hwchase17/react")

# 3. Define the Model using the new class name
model = ChatOllama(model="llama3")

# 4. Create the Agent
agent = create_react_agent(model, tools, prompt)

# 5. Create the Agent Executor with the error handling fix
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True  # <-- This is the key fix
)

# 6. Invoke the Agent
response = agent_executor.invoke(
    {
        "input": "First, find the name of the current prime minister of the UK. Then, find the date they took office."
    }
)

print("\n--- Final Answer ---")
print(response["output"])