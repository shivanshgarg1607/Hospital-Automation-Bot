from playwright.sync_api import sync_playwright
from config import URL, USERNAME, PASSWORD
from image_uploader import upload_image
from image_finder import ImageFinder


class AdminBot:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        self.image_finder = ImageFinder()

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

    def open_hospital_page(self, page=1):

        offset = (page - 1) * 10

        url = (
            "https://karunahealthlifepartner.com/"
            f"Servicemodules/categoryitemSetting/1/{offset}"
        )

        print(f"\nOpening page {page}...")

        self.page.goto(url)

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

    def find_first_placeholder_hospital(self, skipped_hospitals):

        rows = self.get_hospital_rows()

        print()

        for i in range(rows.count()):

            hospital = self.get_hospital_data(rows.nth(i))

            print(f"Checking: {hospital['name']}")

            if hospital["name"] in skipped_hospitals:

                print("Already skipped.")

                continue

            if hospital["image_src"].endswith("hospital.jpg"):

                print("\nPlaceholder hospital found!\n")

                return hospital

        return None
    
    def go_to_next_page(self):

        print("\nChecking for next page...")

        # Current active page number
        active = self.page.locator("li.page-item.active a.page-link")

        if active.count() == 0:

            print("Could not determine current page.")

            return False

        current_page = int(active.inner_text().strip())

        print(f"Current page: {current_page}")

        # Get ALL numbered page links
        links = self.page.locator("li.page-item a.page-link")

        total = links.count()

        best_link = None
        best_number = None

        for i in range(total):

            text = links.nth(i).inner_text().strip()

            if text.isdigit():

                number = int(text)

                if number > current_page:

                    if best_number is None or number < best_number:

                        best_number = number
                        best_link = links.nth(i)

        if best_link:

            print(f"Opening page {best_number}...")

            best_link.click()

            self.page.wait_for_load_state("networkidle")

            return True

        print("No next page.")

        return False
    
    # def go_to_next_page(self):

    #     print("\nChecking for next page...")

    #     next_button = self.page.locator(
    #         "a.page-link",
    #         has_text=">"
    #     )

    #     if next_button.count() == 0:

    #         print("No next page.")

    #         return False

    #     if not next_button.first.is_visible():

    #         print("Next button not visible.")

    #         return False

    #     print("Opening next page...")

    #     next_button.first.click()

    #     self.page.wait_for_load_state("networkidle")

    #     return True

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

    def close_choose_image_modal(self):

        print("\nClosing image dialog...")

        self.page.keyboard.press("Escape")

        self.page.wait_for_timeout(500)

        print("✓ Image dialog closed.")    

    def upload_image(self, hospital):

        image_path = self.image_finder.get_hospital_image(
            hospital["name"]
        )

        if image_path is None:

            print("No image selected.")

            return False

        return upload_image(
            self.page,
            image_path
        )

    def submit_hospital(self):

        print("\n========== submit_hospital() CALLED ==========")

        # input("Press ENTER to continue...")

        print("Trying to find Submit button...")

        submit_button = self.page.locator(
            "button.btn.btn-raised.btn-primary.btn-round.waves-effect"
        )

        # print("Number of matching submit buttons:", submit_button.count())

        submit_button.first.scroll_into_view_if_needed()

        print("Scrolled.")

        # input("Press ENTER before clicking Submit...")

        submit_button.first.click(force=True)

        print("Clicked Submit.")

        self.page.wait_for_load_state("networkidle")

        print("Hospital submitted.")

        return True
    
    
    
    
    
    
    def close(self):

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()