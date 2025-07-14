import requests
from bs4 import BeautifulSoup

def fetch_perplexity_summary(query: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    search_url = f"https://www.perplexity.ai/search?q={query.replace(' ', '+')}"
    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        return f"Error fetching data: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")
    result_blocks = soup.find_all("div", class_="thread-block")

    summary = ""
    for block in result_blocks[:3]:
        text = block.get_text(strip=True)
        summary += f"- {text}\n"

    return summary or "No results parsed."
