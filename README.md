# 🧊 Ice Breaker

This project is a **full-stack generative AI application** that uses LangChain agents, output parsers, and a front-end to generate meaningful icebreaker summaries from LinkedIn profiles. The app takes a **name** as input, searches LinkedIn for the matching profile, extracts and cleans the data, then uses LLMs to summarize it and return structured information.

## 📌 Features

- 🔍 Lookup LinkedIn profiles by name using a LangChain Agent + Tavily search
- 🕸️ Scrape LinkedIn data using Scrapin.io (or mock from GitHub Gist)
- 🧠 Summarize and extract interesting facts using OpenAI's GPT model
- 🔧 Output structured JSON using LangChain Output Parsers
- 🌐 Flask-powered frontend UI

---

## 📁 Project Structure

```
.
├── app.py                   # Flask backend server
├── templates
|   └── index.html           # HTML frontend (served via Flask)
├── ice_breaker.py           # Main business logic: calling agent + scraper + summarizer
├── agents/
│   └── linkedin_lookup_agent.py  # LangChain agent for LinkedIn search
├── third_parties/
│   └── linkedin.py          # Scraper logic using Scrapin.io API
├── tools/
│   └── tools.py             # Tool function for Tavily-based search
├── output_parsers.py        # Pydantic output parser for structured LLM responses
├── Pipfile                  # Python dependencies (use pipenv)
```

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install pipenv
pipenv install
pipenv shell
```

### 2. Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your-openai-key
OPENAI_MODEL_NAME=gpt-4o  # or gpt-3.5-turbo
SCRAPIN_API_KEY=your-scrapin-key
TAVILY_API_KEY=your-tavily-key
```

### 3. Run the Server

```bash
python app.py
```

Navigate to `http://localhost:5000` in your browser.

---

## 🚀 How It Works

### 🔧 Agent (`linkedin_lookup_agent.py`)
- Uses LangChain's **React agent** + **TavilySearch** to look up the LinkedIn profile URL based on a name.

### 🧼 Scraping (`linkedin.py`)
- Uses **Scrapin.io** API to retrieve and clean profile data.

### 🧠 Summarizing (`ice_breaker.py`)
- Builds a prompt for OpenAI to summarize profile info and extract 2 interesting facts.
- Output is structured using Pydantic-based parser.

### 🌍 Frontend (`index.html`)
- Basic form to submit name and view profile summary and facts.

---

## 🧪 Example

### Input:
```
Name: Harrison Chase
```

### Output (JSON):
```json
{
  "summary_and_facts": {
    "summary": "Harrison is the co-founder of LangChain...",
    "facts": [
      "Created LangChain to simplify LLM pipelines.",
      "Previously worked at Robust Intelligence."
    ]
  },
  "picture_url": "https://media.licdn.com/dummy/profile.jpg"
}
```

---

## 📎 Notes

- Use `mock=True` in `linkedin.py` for development with cached responses.
- Improve accuracy by adding more context (e.g., "Eden Marco Udemy").

---

## 📚 References

- [LangChain Docs](https://docs.langchain.com)
- [Scrapin.io](https://scrapin.io)
- [Tavily API](https://app.tavily.com)
- [Flask Docs](https://flask.palletsprojects.com)

---