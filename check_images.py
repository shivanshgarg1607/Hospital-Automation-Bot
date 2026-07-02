from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://karunahealthlifepartner.com/index.php/account/admin")

    page.get_by_role("textbox", name="Enter User Name").fill("karuna__admin")
    page.get_by_role("textbox", name="Password").fill("karuna__admin")
    page.get_by_role("button", name="SIGN IN").click()

    page.get_by_role("link", name="  Services Categories ").click()
    page.get_by_role("link", name=" Hospital").click()

    page.wait_for_timeout(3000)

    images = page.locator("table img")

    print("Number of images:", images.count())

    for i in range(images.count()):

        img = images.nth(i)

        print("--------------------")
        print("IMAGE", i)
        print("SRC:", img.get_attribute("src"))
        print("ALT:", img.get_attribute("alt"))
        print("CLASS:", img.get_attribute("class"))

    input("Press ENTER...")

    browser.close()