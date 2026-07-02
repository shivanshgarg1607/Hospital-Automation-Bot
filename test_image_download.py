import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

website = "https://www.vinayakhospitalnoida.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print(f"Opening {website}")

response = requests.get(website, headers=headers)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

images = soup.find_all("img")

print(f"\nFound {len(images)} images\n")

for i, img in enumerate(images, start=1):

    src = img.get("src")

    if not src:
        continue

    full_url = urljoin(website, src)

    print(i, full_url)