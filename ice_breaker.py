import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()

if __name__ == "__main__":
    print("Hello World")

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

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="mock",
        mock=True,
    )

    response = chain.invoke(input={"information": linkedin_data})
    print(response)