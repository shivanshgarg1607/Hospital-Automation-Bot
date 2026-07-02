from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.google.com")

    input("Accept cookies if needed, then press ENTER here...")

    page.goto("https://www.google.com/search?q=Vinayak+Hospital+Noida+official+website")

    input("When results are visible, press ENTER...")

    print(page.content())

    browser.close()