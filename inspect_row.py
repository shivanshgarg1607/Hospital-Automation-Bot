from playwright.sync_api import sync_playwright
from config import URL, USERNAME, PASSWORD


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(URL)

    page.get_by_role(
        "textbox",
        name="Enter User Name"
    ).fill(USERNAME)

    page.get_by_role(
        "textbox",
        name="Password"
    ).fill(PASSWORD)

    page.get_by_role(
        "button",
        name="SIGN IN"
    ).click()

    page.wait_for_load_state("networkidle")

    page.get_by_role(
        "link",
        name="  Services Categories "
    ).click()

    page.get_by_role(
        "link",
        name=" Hospital"
    ).click()

    page.wait_for_load_state("networkidle")

    row = page.locator("table tbody tr").nth(4)

    print("\n" + "=" * 80)
    print("ROW HTML")
    print("=" * 80)
    print(row.inner_html())

    print("\nPress ENTER to close...")

    input()

    browser.close()