from langchain_tavily.tavily_search import TavilySearch

def get_profile_url_tavily(name: str):
    """Searches for Linkedin or Twitter Profile page."""
    search = TavilySearch()
    res = search.run(f"{name}")
    result = res["results"][0]["url"]

    return result