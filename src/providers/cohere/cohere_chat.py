import os

from langchain.agents import AgentExecutor
from langchain_cohere import ChatCohere
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate

from src.config.msecrets import COHERE_API_KEY, TAVILY_API_KEY
from src.stores.smsmagic import smsmagic_retriever_tool

# Create search tool
os.environ['TAVILY_API_KEY'] = TAVILY_API_KEY
internet_search = TavilySearchResults()

# Create LLM model
llm = ChatCohere(cohere_api_key=COHERE_API_KEY)

# Create an agent for  answering questions
agent = create_cohere_react_agent(
    llm=llm,
    tools=[smsmagic_retriever_tool, internet_search],
    prompt=ChatPromptTemplate.from_template("{question}"),
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[smsmagic_retriever_tool, internet_search],
    verbose=True
)

# response = agent_executor.invoke({
#     "question": "What is SMS-Magic Web Portal?",
# })
#
# # See Cohere's response
# print(response.get("output"))
# Cohere provides exact citations for the sources it used
# print(response.get("citations"))
