import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()

def ice_break_with(name: str):
    summary_template = """
            given the Linkedin information {information} about a person I want you to create:
            1. A short summary
            2. two interesting facts about them
            """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        model=os.getenv("OPENAI_MODEL_NAME"),
    )

    chain = summary_prompt_template | llm

    linkedin_profile = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile,
        # mock=True, # True for using mock data
    )

    response = chain.invoke(input={"information": linkedin_data})
    print(response)

if __name__ == "__main__":
    print("Ice Breaker Enter")
    ice_break_with("Arif Hidayatullah")