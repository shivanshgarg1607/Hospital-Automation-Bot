from playwright.sync_api import sync_playwright
from config import URL, USERNAME, PASSWORD


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    # Login
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

    # Open Vinayak Hospital edit page directly
    page.goto(
        "https://karunahealthlifepartner.com/servicemodules/editcategoryitem/1893/"
    )

    page.wait_for_load_state("networkidle")

    print("\n" + "=" * 80)
    print("FILE INPUTS")
    print("=" * 80)

    file_inputs = page.locator("input[type='file']")

    print("Count:", file_inputs.count())

    for i in range(file_inputs.count()):

        print("\n---------- FILE INPUT", i, "----------")
        print(file_inputs.nth(i).evaluate(
            "(element) => element.outerHTML"
        ))

    print("\n" + "=" * 80)
    print("BUTTONS")
    print("=" * 80)

    buttons = page.locator("button")

    print("Count:", buttons.count())

    for i in range(buttons.count()):

        button = buttons.nth(i)

        print("\n---------- BUTTON", i, "----------")

        print(button.evaluate(
            "(element) => element.outerHTML"
        ))

    input("\nPress ENTER to close...")

    browser.close()