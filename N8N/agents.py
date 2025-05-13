from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from decouple import config
import os
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

# create LLM model
os.environ["OPENAI_API_KEY"] = "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"

OPENAI_API_KEY= os.getenv("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")
llm = ChatOpenAI(model_name='gpt-3.5-turbo')

llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

# connect to our database
db = SQLDatabase.from_uri("mysql+pymysql://root:benja122@localhost:3306/n8n")

# create the database chain
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

tools = [
    Tool(
        name="MathTool",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    ),
    Tool(
        name="Product_Database",
        func=db_chain.run,
        description="useful for when you need to answer questions about products."
    )
]

# creating the agent
agent = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

# ask the LLM a question
respuesta = agent.run("Que tengo en mi base de datos")
print(respuesta)