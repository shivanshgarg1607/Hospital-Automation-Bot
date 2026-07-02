# # import os
# # from urllib.parse import urljoin

# # import requests
# # from bs4 import BeautifulSoup

# # from web_search import WebSearch


# # class ImageFinder:

# #     def __init__(self):
# #         self.search = WebSearch(headless=True)

# #     def get_hospital_image(self, hospital_name, city=""):

# #         website = self.search.search(hospital_name, city)

# #         if not website:
# #             print("No website found.")
# #             return None

# #         print(f"\nWebsite: {website}")

# #         try:

# #             response = requests.get(
# #                 website,
# #                 timeout=20,
# #                 headers={
# #                     "User-Agent":
# #                     "Mozilla/5.0"
# #                 }
# #             )

# #         except Exception as e:

# #             print(e)
# #             return None

# #         soup = BeautifulSoup(response.text, "html.parser")

# #         images = soup.find_all("img")

# #         print(f"\nFound {len(images)} images")

# #         image_urls = []

# #         for image in images:

# #             src = image.get("src")

# #             if not src:
# #                 continue

# #             full_url = urljoin(website, src)

# #             image_urls.append(full_url)

# #         if not image_urls:

# #             print("No images found.")

# #             return None

# #         os.makedirs("downloads", exist_ok=True)

# #         first_image = image_urls[0]

# #         print("\nDownloading:")
# #         print(first_image)

# #         image = requests.get(first_image)

# #         filename = os.path.join(
# #             "downloads",
# #             hospital_name + ".jpg"
# #         )

# #         with open(filename, "wb") as f:

# #             f.write(image.content)

# #         print("\nDownloaded:")
# #         print(filename)

# #         return filename

# #     def close(self):

# #         self.search.close()







# import os
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# from pathlib import Path


# class ImageFinder:

#     def __init__(self):

#         self.headers = {
#             "User-Agent": (
#                 "Mozilla/5.0 "
#                 "(Windows NT 10.0; Win64; x64) "
#                 "AppleWebKit/537.36 "
#                 "(KHTML, like Gecko) "
#                 "Chrome/137.0 Safari/537.36"
#             )
#         }

#         self.search_url = "https://html.duckduckgo.com/html/"

#         self.download_folder = Path("downloads")
#         self.download_folder.mkdir(exist_ok=True)

#     # -------------------------------------------------------------

#     def get_hospital_image(self, hospital_name, city=""):

#         print("\n==============================")
#         print("IMAGE FINDER")
#         print("==============================")

#         website = self.search_official_website(
#             hospital_name,
#             city
#         )

#         if website is None:
#             print("Official website not found.")
#             return None

#         print(f"\nOfficial Website:\n{website}")

#         pages = self.find_gallery_pages(website)

#         if website not in pages:
#             pages.insert(0, website)

#         print("\nPages to inspect:")

#         for page in pages:
#             print(" -", page)

#         image_urls = []

#         for page in pages:

#             urls = self.collect_images(page)

#             image_urls.extend(urls)

#         image_urls = list(dict.fromkeys(image_urls))

#         print(f"\nCollected {len(image_urls)} unique images.")

#         if len(image_urls) == 0:
#             return None

#         best_images = self.choose_best_images(image_urls)

#         if best is None:
#             return None

#         print("\nSelected image:")
#         print(best)

        

#     # -------------------------------------------------------------

#     def search_official_website(self, hospital_name, city=""):

#         query = hospital_name

#         if city:
#             query += " " + city

#         query += " official website"

#         print("\nSearching DuckDuckGo:")
#         print(query)

#         response = requests.post(
#             self.search_url,
#             data={"q": query},
#             headers=self.headers,
#             timeout=30
#         )

#         soup = BeautifulSoup(
#             response.text,
#             "html.parser"
#         )

#         results = soup.select(".result__title a")

#         for result in results:

#             href = result.get("href")

#             if not href:
#                 continue

#             href = href.strip()

#             if href.startswith("http"):
#                 return href

#         return None

#     # -------------------------------------------------------------

#     def find_gallery_pages(self, website):

#         print("\nSearching for gallery pages...")

#         try:

#             response = requests.get(
#                 website,
#                 headers=self.headers,
#                 timeout=30
#             )

#         except Exception:

#             return []

#         soup = BeautifulSoup(
#             response.text,
#             "html.parser"
#         )

#         keywords = [

#             "gallery",
#             "gallary",
#             "photo",
#             "photos",
#             "image",
#             "images",
#             "media",
#             "facility",
#             "facilities",
#             "campus",
#             "infrastructure"

#         ]

#         pages = []

#         for a in soup.find_all("a"):

#             href = a.get("href")

#             if not href:
#                 continue

#             text = (
#                 a.get_text(" ", strip=True)
#                 + " "
#                 + href
#             ).lower()

#             for word in keywords:

#                 if word in text:

#                     full = urljoin(
#                         website,
#                         href
#                     )

#                     if full not in pages:
#                         pages.append(full)

#                     break

#         return pages
    

#     # -------------------------------------------------------------

#     def collect_images(self, page_url):

#         print(f"\nScanning images from:\n{page_url}")

#         try:

#             response = requests.get(
#                 page_url,
#                 headers=self.headers,
#                 timeout=30
#             )

#         except Exception as e:

#             print(e)
#             return []

#         soup = BeautifulSoup(
#             response.text,
#             "html.parser"
#         )

#         image_urls = []

#         for img in soup.find_all("img"):

#             src = img.get("src")

#             if not src:
#                 continue

#             src = src.strip()

#             if src == "":
#                 continue

#             full = urljoin(
#                 page_url,
#                 src
#             )

#             image_urls.append(full)

#         print(f"Found {len(image_urls)} images.")

#         return image_urls

#     # -------------------------------------------------------------

#     def choose_best_images(self, image_urls):

#         print("\nScoring images...")

#         scored = []

#         bad_words = [

#             "logo",
#             "icon",
#             "doctor",
#             "staff",
#             "facebook",
#             "instagram",
#             "twitter",
#             "linkedin",
#             "department",
#             "speciality",
#             "specialty"

#         ]

#         good_words = [

#             "gallery",
#             "building",
#             "hospital",
#             "campus",
#             "front",
#             "banner",
#             "outside",
#             "main"

#         ]

#         for url in image_urls:

#             score = 0

#             lower = url.lower()

#             for word in good_words:

#                 if word in lower:
#                     score += 20

#             for word in bad_words:

#                 if word in lower:
#                     score -= 50

#             if lower.endswith(".jpg"):
#                 score += 10

#             if lower.endswith(".jpeg"):
#                 score += 10

#             if lower.endswith(".png"):
#                 score += 5

#             filename = os.path.basename(lower)

#             if filename[:1].isdigit():
#                 score += 15

#             scored.append(
#                 (
#                     score,
#                     url
#                 )
#             )

#         scored.sort(
#             reverse=True,
#             key=lambda x: x[0]
#         )

#         print("\nTop candidates:")

#         for score, url in scored[:10]:

#             print(
#                 f"{score:>4}  {url}"
#             )

#         if len(scored) == 0:
#             return None

#         return [url for score, url in scored[:3]]

#     # -------------------------------------------------------------

#     def download_image(
#         self,
#         image_url,
#         hospital_name
#     ):

#         print("\nDownloading image...")

#         extension = ".jpg"

#         lower = image_url.lower()

#         if ".png" in lower:
#             extension = ".png"

#         elif ".jpeg" in lower:
#             extension = ".jpeg"

#         filename = (
#             hospital_name
#             .replace("/", "-")
#             .replace("\\", "-")
#             .strip()
#             + extension
#         )

#         save_path = (
#             self.download_folder /
#             filename
#         )

#         try:

#             response = requests.get(
#                 image_url,
#                 headers=self.headers,
#                 timeout=60,
#                 stream=True
#             )    



#             response.raise_for_status()

#             with open(save_path, "wb") as file:

#                 for chunk in response.iter_content(8192):

#                     if chunk:
#                         file.write(chunk)

#             print("\nImage downloaded successfully.")
#             print(save_path)

#             return str(save_path)

#         except Exception as e:

#             print("\nFailed to download image.")
#             print(e)

#             return None


# # -------------------------------------------------------------
# # Test
# # -------------------------------------------------------------

# if __name__ == "__main__":

#     finder = ImageFinder()

#     image = finder.get_hospital_image(
#         hospital_name="Vinayak Hospital",
#         city="Noida"
#     )

#     print("\nReturned image path:")
#     print(image)            



import os
import shutil
import requests
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup


class ImageFinder:

    def __init__(self):

        self.headers = {
            "User-Agent":
            (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/137.0 Safari/537.36"
            )
        }

        self.search_url = "https://html.duckduckgo.com/html/"

        self.download_folder = Path("downloads")

        self.temp_folder = self.download_folder / "temp"

        self.download_folder.mkdir(exist_ok=True)
        self.temp_folder.mkdir(exist_ok=True)

    # ============================================================
    # PUBLIC FUNCTION
    # ============================================================

    def get_hospital_image(
        self,
        hospital_name,
        city=""
    ):

        print("\n========================================")
        print("IMAGE FINDER")
        print("========================================")

        final_image = (
            self.download_folder /
            f"{hospital_name}.jpg"
        )

        # ------------------------------------
        # Already downloaded?
        # ------------------------------------

        if final_image.exists():

            print("\nImage already exists.")

            print(final_image)

            return str(final_image)

        # ------------------------------------
        # Search website
        # ------------------------------------

        website = self.search_official_website(
            hospital_name,
            city
        )

        if website is None:

            print("\nWebsite not found.")

            return None

        print("\nOfficial Website")
        print(website)

        # ------------------------------------
        # Find gallery pages
        # ------------------------------------

        pages = self.find_gallery_pages(
            website
        )

        if website not in pages:
            pages.insert(0, website)

        print("\nPages found:")

        for page in pages:

            print(" -", page)

        # ------------------------------------
        # Collect images
        # ------------------------------------

        image_urls = []

        for page in pages:

            image_urls.extend(
                self.collect_images(page)
            )

        image_urls = list(
            dict.fromkeys(image_urls)
        )

        print(
            f"\nCollected {len(image_urls)} unique images."
        )

        if len(image_urls) == 0:

            return None

        # ------------------------------------
        # Rank images
        # ------------------------------------

        best_images = self.choose_best_images(
            image_urls,
            count=5
        )

        print("\nTop Candidates")

        for i, image in enumerate(best_images, start=1):

            print(f"{i}. {image}")

        # ------------------------------------
        # Download candidates
        # ------------------------------------

        downloaded = self.download_candidates(
            best_images
        )

        if len(downloaded) == 0:

            print("Nothing downloaded.")

            return None

        return self.choose_candidate(
            downloaded,
            hospital_name
        )

    # ============================================================
    # SEARCH WEBSITE
    # ============================================================

    def search_official_website(
        self,
        hospital_name,
        city=""
    ):

        query = hospital_name

        if city:

            query += " " + city

        query += " official website"

        print("\nSearching:")
        print(query)

        response = requests.post(
            self.search_url,
            data={
                "q": query
            },
            headers=self.headers,
            timeout=30
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        results = soup.select(
            ".result__title a"
        )

        for result in results:

            href = result.get("href")

            if href and href.startswith("http"):

                return href

        return None
    
    # ============================================================
    # FIND GALLERY PAGES
    # ============================================================

    def find_gallery_pages(self, website):

        print("\nSearching for gallery pages...")

        try:

            response = requests.get(
                website,
                headers=self.headers,
                timeout=30
            )

        except Exception:

            return []

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        keywords = [

            "gallery",
            "gallary",
            "photo",
            "photos",
            "image",
            "images",
            "facility",
            "facilities",
            "campus",
            "media",
            "infrastructure"

        ]

        pages = []

        for a in soup.find_all("a"):

            href = a.get("href")

            if not href:
                continue

            text = (
                a.get_text(" ", strip=True)
                + " "
                + href
            ).lower()

            for keyword in keywords:

                if keyword in text:

                    full = urljoin(
                        website,
                        href
                    )

                    if full not in pages:
                        pages.append(full)

                    break

        return pages

    # ============================================================
    # COLLECT IMAGE URLS
    # ============================================================

    def collect_images(self, page_url):

        print(f"\nScanning:\n{page_url}")

        try:

            response = requests.get(
                page_url,
                headers=self.headers,
                timeout=30
            )

        except Exception as e:

            print(e)

            return []

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        image_urls = []

        for img in soup.find_all("img"):

            src = img.get("src")

            if not src:
                continue

            src = src.strip()

            if src == "":
                continue

            full = urljoin(
                page_url,
                src
            )

            image_urls.append(full)

        print(
            f"Found {len(image_urls)} images."
        )

        return image_urls

    # ============================================================
    # SCORE IMAGES
    # ============================================================

    def choose_best_images(
        self,
        image_urls,
        count=5
    ):

        print("\nScoring images...")

        scored = []

        bad_words = [

            "logo",
            "icon",
            "doctor",
            "staff",
            "facebook",
            "twitter",
            "linkedin",
            "instagram",
            "department",
            "speciality",
            "specialty"

        ]

        good_words = [

            "gallery",
            "building",
            "hospital",
            "front",
            "campus",
            "outside",
            "main",
            "photo"

        ]

        for url in image_urls:

            score = 0

            lower = url.lower()

            for word in good_words:

                if word in lower:
                    score += 20

            for word in bad_words:

                if word in lower:
                    score -= 50

            if lower.endswith(".jpg"):
                score += 10

            if lower.endswith(".jpeg"):
                score += 10

            if lower.endswith(".png"):
                score += 5

            filename = os.path.basename(lower)

            if filename and filename[0].isdigit():
                score += 15

            scored.append(
                (
                    score,
                    url
                )
            )

        scored.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        print("\nRanking")

        for score, url in scored[:count]:

            print(f"{score:>4}  {url}")

        return [

            url

            for score, url

            in scored[:count]

        ]

    # ============================================================
    # DOWNLOAD TOP CANDIDATES
    # ============================================================

    def download_candidates(self, image_urls):

        print("\nDownloading candidate images...")

        # ----------------------------------------
        # Clear old temp folder
        # ----------------------------------------

        if self.temp_folder.exists():

            shutil.rmtree(self.temp_folder)

        self.temp_folder.mkdir(exist_ok=True)

        downloaded = []

        for index, url in enumerate(image_urls, start=1):

            extension = ".jpg"

            lower = url.lower()

            if ".png" in lower:
                extension = ".png"

            elif ".jpeg" in lower:
                extension = ".jpeg"

            filename = f"{index}{extension}"

            save_path = self.temp_folder / filename

            try:

                response = requests.get(
                    url,
                    headers=self.headers,
                    timeout=60,
                    stream=True
                )

                response.raise_for_status()

                with open(save_path, "wb") as file:

                    for chunk in response.iter_content(8192):

                        if chunk:
                            file.write(chunk)

                downloaded.append(save_path)

                print(f"✓ {filename}")

            except Exception as e:

                print(f"✗ Failed: {url}")
                print(e)

        return downloaded

    # ============================================================
    # LET USER CHOOSE IMAGE
    # ============================================================

    def choose_candidate(
        self,
        downloaded,
        hospital_name
    ):

        print("\n========================================")
        print("CANDIDATE IMAGES READY")
        print("========================================")

        print("\nOpening folder...")

        os.startfile(self.temp_folder)

        print("\nDownloaded images:\n")

        for i, image in enumerate(downloaded, start=1):

            print(f"{i}. {image.name}")

        while True:

            choice = input(
                "\nChoose image (1-5): "
            ).strip()

            if not choice.isdigit():

                print("Please enter a number.")

                continue

            choice = int(choice)

            if choice < 1 or choice > len(downloaded):

                print("Invalid choice.")

                continue

            break

        selected = downloaded[choice - 1]

        extension = selected.suffix

        final_image = (
            self.download_folder /
            f"{hospital_name}{extension}"
        )

        shutil.move(selected, final_image)

        print("\nSelected image saved as:")

        print(final_image)

        # ----------------------------------------
        # Delete temp folder
        # ----------------------------------------

        shutil.rmtree(self.temp_folder)

        return str(final_image)


    # ============================================================
    # CLEAN HOSPITAL NAME
    # ============================================================

    def clean_filename(self, hospital_name):

        invalid = '<>:"/\\|?*'

        for ch in invalid:
            hospital_name = hospital_name.replace(ch, "-")

        return hospital_name.strip()

    # ============================================================
    # DOWNLOAD IF ALREADY EXISTS
    # ============================================================

    def get_existing_image(self, hospital_name):

        hospital_name = self.clean_filename(hospital_name)

        for ext in [".jpg", ".jpeg", ".png"]:

            path = self.download_folder / f"{hospital_name}{ext}"

            if path.exists():

                return str(path)

        return None


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    finder = ImageFinder()

    image = finder.get_hospital_image(

        hospital_name="Vinayak Hospital",
        city="Noida"

    )

    print("\n========================================")
    print("FINAL RESULT")
    print("========================================")

    print(image)            