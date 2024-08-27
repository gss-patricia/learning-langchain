from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleSequentialChain
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), 
                  model="gpt-3.5-turbo", 
                  temperature=0.5)

template_city = ChatPromptTemplate.from_template("Sugira uma cidade dado meu interesse por {interesse}. A sua saida deve ser SOMENTE o nome da cidade. Cidade: ")
template_restaurants = ChatPromptTemplate.from_template("Sugira restaurante populares entre local em {cidade}")
template_cultural = ChatPromptTemplate.from_template("Sugira atividades e locais culturais em {cidade}")

chain_cidade = LLMChain(prompt=template_city, llm=llm)
chain_restaurants = LLMChain(prompt=template_restaurants, llm=llm)
chain_cultural = LLMChain(prompt=template_cultural, llm=llm)

chain = SimpleSequentialChain(chains=[chain_cidade, chain_restaurants, chain_cultural], verbose=True)

result = chain.invoke("praias")

print(result)