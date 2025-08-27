from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama

# 1. Create a prompt template
prompt_template = ChatPromptTemplate.from_template(
    "You are a helpful AI assistant. Answer the user's question: {input}"
)

# 2. Connect to our local Ollama model
model = ChatOllama(model="llama3")

# 3. Create a simple output parser
output_parser = StrOutputParser()

# 4. Set up the chain
chain = prompt_template | model | output_parser

# 5. Run the chain with our input
response = chain.invoke({"input": "What is an LLM?"})

print(response)