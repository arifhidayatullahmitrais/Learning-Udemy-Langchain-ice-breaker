import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from tools.tools import get_profile_url_tavily

load_dotenv()

def lookup(name: str) -> str:
    llm = ChatOpenAI(
        api_key=os.environ["OPENAI_API_KEY"],
        model=os.environ["OPENAI_MODEL_NAME"],
    )

    template = """give the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
    Your answer should contain only URL"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the Linkedin Page Url"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    return result["output"]

if __name__ == "__main__":
    linkedin_url = lookup("arif hidayatullah")
