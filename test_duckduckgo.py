import requests
from bs4 import BeautifulSoup

query = "Vinayak Hospital Noida official website"

url = "https://html.duckduckgo.com/html/"

response = requests.post(
    url,
    data={"q": query},
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

results = soup.select(".result__title a")

print(f"\nFound {len(results)} results\n")

for i, result in enumerate(results[:5], start=1):
    print(i)
    print(result.get_text(strip=True))
    print(result.get("href"))
    print("-" * 50)