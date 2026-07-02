from pathlib import Path
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://duckduckgo.com")

    page.fill('input[name="q"]', "Vinayak Hospital Noida")

    page.keyboard.press("Enter")

    input("When the search results appear, press ENTER in the terminal...")

    output_file = Path(__file__).parent / "duckduckgo_results.html"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(page.content())

    print("\nHTML saved successfully!")
    print(f"Location: {output_file.resolve()}")

    browser.close()