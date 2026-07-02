from playwright.sync_api import sync_playwright


class WebSearch:

    def __init__(self, headless=False):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=headless
        )
        self.page = self.browser.new_page()

    def search(self, hospital_name, city=""):

        query = f"{hospital_name} {city} official website"

        print(f"\nSearching: {query}")

        self.page.goto("https://duckduckgo.com")

        self.page.locator("input[name='q']").fill(query)

        self.page.keyboard.press("Enter")

        # Wait until the first search result appears
        self.page.wait_for_selector(
            "a[data-testid='result-title-a']",
            timeout=60000
        )

        first_result = self.page.locator(
            "a[data-testid='result-title-a']"
        ).first



        title = first_result.text_content()

        url = first_result.evaluate("(el) => el.href")

        print("\nFirst Result")
        print("----------------------------")
        print("Title :", title)
        print("URL   :", url)

        return url

    def close(self):

        self.browser.close()

        self.playwright.stop()
