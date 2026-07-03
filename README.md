# Hospital Automation Bot

## Overview

Hospital Automation Bot is a Python automation tool built using Playwright.

It automatically finds hospitals with placeholder images in the admin panel, searches the hospital's official website, downloads candidate images, allows manual selection, uploads the chosen image, submits the form, and continues through all pages.

---

## Features

- Automatic Login
- Placeholder Image Detection
- DuckDuckGo Search
- Official Website Detection
- Gallery Image Extraction
- Image Download
- Manual Image Selection
- Automatic Upload
- Automatic Form Submission
- Multi-page Navigation
- Missing Hospital Logging

---

## Technologies

- Python
- Playwright
- Requests
- BeautifulSoup
- Pillow

---

## Installation

Install requirements

```bash
pip install -r requirements.txt
Install Playwright
python -m playwright install
Run
python main.py


Project Structure

main.py

Main automation loop.

admin.py

Browser automation.

image_finder.py

Searches hospital images.

image_uploader.py

Uploads images.

web_search.py

Finds official website.

missing_logger.py

Logs skipped hospitals.

Future Improvements
SQLite Database
GUI
AI Image Ranking
Resume Automation
Automatic Image Selection