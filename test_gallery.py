import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://www.vinayakhospitalnoida.com/gallary_2.html"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

images = soup.find_all("img")

print(f"\nFound {len(images)} images\n")

for i, img in enumerate(images, 1):
    src = img.get("src")
    if not src:
        continue

    print(i, urljoin(url, src))