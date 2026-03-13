import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS


def search_web(query, num_results=3):
    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(query, max_results=num_results)

        for r in search_results:
            url = r["href"]

            try:
                response = requests.get(url, timeout=5)
                soup = BeautifulSoup(response.text, "html.parser")

                paragraphs = soup.find_all("p")
                text = " ".join([p.get_text() for p in paragraphs[:10]])

                results.append(text)

            except:
                continue

    return results