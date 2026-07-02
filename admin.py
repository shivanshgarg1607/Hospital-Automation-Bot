from playwright.sync_api import sync_playwright
from config import URL, USERNAME, PASSWORD
from image_uploader import upload_image


class AdminBot:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def launch_browser(self, headless=False):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=headless
        )

        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def login(self):
        self.page.goto(URL)

        self.page.get_by_role(
            "textbox",
            name="Enter User Name"
        ).fill(USERNAME)

        self.page.get_by_role(
            "textbox",
            name="Password"
        ).fill(PASSWORD)

        self.page.get_by_role(
            "button",
            name="SIGN IN"
        ).click()

        self.page.wait_for_load_state("networkidle")

    def open_hospital_page(self):

        self.page.get_by_role(
            "link",
            name="  Services Categories "
        ).click()

        self.page.get_by_role(
            "link",
            name=" Hospital"
        ).click()

        self.page.wait_for_load_state("networkidle")

    def get_hospital_rows(self):
        return self.page.locator("table tbody tr")

    def get_hospital_data(self, row):

        cells = row.locator("td")

        image = cells.nth(1).locator("img")
        image_src = image.get_attribute("src") or ""

        hospital_name = (
            cells.nth(2)
            .text_content()
            .replace("updated", "")
            .strip()
        )

        edit_url = (
            row.locator("a", has_text="Edit")
            .get_attribute("href")
        )

        return {
            "name": hospital_name,
            "image_src": image_src,
            "edit_url": edit_url,
            "row": row
        }

    def find_first_placeholder_hospital(self):

        rows = self.get_hospital_rows()

        print()

        for i in range(rows.count()):

            hospital = self.get_hospital_data(rows.nth(i))

            print(f"Checking: {hospital['name']}")

            if hospital["image_src"].endswith("hospital.jpg"):

                print("\nPlaceholder hospital found!\n")

                return hospital

        return None

    def open_edit_page(self, hospital):

        print(f"\nOpening edit page for: {hospital['name']}")

        self.page.goto(hospital["edit_url"])

        self.page.wait_for_load_state("networkidle")

        print("✓ Edit page opened successfully.")

    def open_choose_image_modal(self):

        print("\nOpening image dialog...")

        self.page.get_by_role(
            "button",
            name="Choose Image"
        ).click()

        self.page.wait_for_timeout(1000)

        print("✓ Image dialog opened.")

    def upload_image(self):

        return upload_image(self.page)

    def close(self):

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()