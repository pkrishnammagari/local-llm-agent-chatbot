# 🤖 Local LLM Agent Chatbot

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.2-green.svg)

A sophisticated chatbot application that runs a local Large Language Model (Llama 3) and enhances its capabilities with an agentic framework, allowing it to access external tools like a live web search.

---

### 📸 Demo

![App Demo Screenshot](https://github.com/pkrishnammagari/local-llm-agent-chatbot/blob/main/Screenshot%202025-08-27%20at%2012.59.58.png)

### ✨ Features

* **Local & Private**: Runs the Llama 3 8B model entirely on your local machine using Ollama, ensuring 100% privacy.
* **Web Interface**: A clean and interactive chat interface built with Streamlit, featuring a full conversation history.
* **Agentic Framework**: Uses LangChain to transform the LLM from a simple chatbot into a reasoning agent.
* **Live Web Search**: The agent can use the Tavily Search API as a tool to answer questions about recent events, overcoming the LLM's knowledge cutoff.
* **Robust & Modular Code**: Refactored using LangChain's components (`PromptTemplates`, `Chains`, `Agents`) for a professional, easy-to-maintain codebase.

---

### 🛠️ Tech Stack

* **Language**: Python 3.11+
* **LLM Serving**: Ollama
* **LLM**: Llama 3 8B
* **Web Framework**: Streamlit
* **AI Framework**: LangChain
* **Tools**: Tavily Search API

---

### 🚀 Local Setup & Installation

Follow these steps to run the project on your own machine.

**1. Clone the Repository**
```bash
git clone [Your-GitHub-Repo-URL]
cd [your-repo-name]
```

**2. Set Up the Environment**
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the environment (macOS/Linux)
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Set Up Ollama**
* Download and install [Ollama](https://ollama.com/).
* Pull the Llama 3 model from the command line:
    ```bash
    ollama pull llama3
    ```

**5. Get API Keys**
* Sign up for a free API key at [Tavily.com](https://tavily.com/).

**6. Run the Application**
* Set your Tavily API key as an environment variable in your terminal:
    ```bash
    export TAVILY_API_KEY="your_key_here"
    ```
* Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

---

### 🧠 What I Learned

This project was a deep dive into building modern AI applications. Key takeaways include:

* **Agentic AI**: Moving beyond basic LLM calls to create agents that can reason and use tools is a paradigm shift in building capable AI.
* **Prompt Engineering**: The agent's performance is highly dependent on the quality of its instructions. Iteratively improving the prompt was key to getting the correct results.
* **The Power of Frameworks**: LangChain abstracts away immense complexity, allowing for the rapid development of sophisticated, multi-step AI logic.
* **Local LLM Deployment**: Gained hands-on experience with running and interacting with powerful open-source models locally using Ollama.
