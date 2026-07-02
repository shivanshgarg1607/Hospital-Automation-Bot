from web_search import WebSearch

search = WebSearch(headless=False)

search.page.goto("https://duckduckgo.com")

search.page.locator("input[name='q']").fill(
    "Vinayak Hospital Noida official website"
)

search.page.keyboard.press("Enter")

print("Search complete.")

input("\nPress ENTER after the results page has fully loaded...")

search.close()