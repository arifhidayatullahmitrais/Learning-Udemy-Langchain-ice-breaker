import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    scrape information from LikedIn profiles,
    Manually scrape the information from the LinkedIn profile
    """
    try:
        if mock:
            linkedin_profile_url = "https://gist.githubusercontent.com/arifdegozaru/db7e6caf407214411df64e6d45917dcc/raw/d05bde900f97243295be950e027cd46a299f73bf/arif-hidayatullah-scrapin.json"
            response = requests.get(linkedin_profile_url, timeout=10)
        else:
            api_endpoint = "https://api.scrapin.io/enrichment/profile"
            params = {
                "apikey": os.environ["SCRAPIN_API_KEY"],
                "linkedInUrl": linkedin_profile_url,
            }
            response = requests.get(
                api_endpoint,
                params=params,
                timeout=10,
            )

        data = response.json().get("person")
        data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", "", None) and k not in ["certifications"]
        }

        return data
    except Exception:
        return {}


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/arif-hidayatulah-4817a5a8",
            mock=True,
        )
    )
