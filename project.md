# 🏥 Hospital Automation Bot
Version: 1.0 MVP

Author: Shivansh Garg
Mentor: ChatGPT

---

# Objective

Build a reusable Python automation tool that automatically uploads hospital images to the Karuna Health Life Partner admin panel.

The long-term goal is to automate the complete workflow with minimal human intervention while keeping the project modular and reusable for future freelancing work.

---

# Website

Login URL

https://karunahealthlifepartner.com/index.php/account/admin

Username

karuna__admin

Password

Stored in config.py

---

# Current Progress

## Completed

- [x] Python environment setup
- [x] VS Code setup
- [x] Playwright installed
- [x] Browser automation working
- [x] Automatic login working
- [x] Automatic navigation to Hospital page
- [x] Successfully read all hospital rows
- [x] Understood upload workflow
- [x] Understood pagination
- [x] Identified placeholder image

---

# Important Discovery

Hospitals WITHOUT uploaded photos use exactly the same image.

Image source:

hospital.jpg

Example

https://karunahealthlifepartner.com/uploads/hospital.jpg

Therefore:

if image_src.endswith("hospital.jpg"):

↓

Hospital requires upload.

Otherwise

↓

Skip.

This discovery reduces work dramatically because the bot only processes hospitals that actually need images.

---

# Website Workflow

Login

↓

Services Categories

↓

Hospital

↓

Hospital List

↓

For every row

↓

Check image

↓

If image == hospital.jpg

↓

Three dots

↓

Edit

↓

Choose Image

↓

Add New Image

↓

Upload

↓

Submit (popup)

↓

Scroll down

↓

Submit (Hospital page)

↓

Automatically returns to Hospital List

↓

Continue

---

# Pagination

Page URLs

/categoryitemSetting/1

/categoryitemSetting/1/10

/categoryitemSetting/1/20

/categoryitemSetting/1/30

The last number appears to be the row offset.

Instead of clicking pagination buttons the bot should generate URLs directly.

---

# Project Structure

HOSPITALAUTOMATION/

│

├── main.py

├── admin.py

├── image_finder.py

├── logger.py

├── utils.py

├── config.py

│

├── downloads/

├── logs/

├── screenshots/

├── PROJECT.md

└── requirements.txt

---

# Modules

## main.py

Starts the application.

Coordinates all modules.

---

## admin.py

Responsible for

- Login
- Hospital navigation
- Edit hospital
- Upload image
- Submit
- Pagination

---

## image_finder.py

Responsible for

Input

Hospital Name

Output

downloads/Hospital Name.jpg

Long-term goal

Search official website

↓

Find best hospital image

↓

Download

↓

Return local path

---

## logger.py

Maintain

uploaded.csv

Columns

Hospital Name

Image File

Page Number

Status

Timestamp

Reason (if failed)

---

## utils.py

Utility functions

Examples

sanitize_filename()

scroll_to_submit()

safe_click()

wait_for_page()

---

# MVP Goals

Phase 1

- Login
- Hospital page
- Skip uploaded hospitals
- Upload local images
- Submit
- Log results

Phase 2

Automatic image downloading

Hospital Name

↓

Search

↓

Official website

↓

Download image

↓

Upload

---

# Long-Term Goals

- Resume after crash
- GUI
- Progress bar
- Multi-threaded image downloading
- Automatic retries
- AI-assisted image ranking
- EXE build
- Client-ready software

---

# Coding Principles

- Modular code
- No duplicated logic
- Reusable functions
- Production-quality structure
- Keep selectors centralized
- Never hardcode hospital names

---

# Current Automation Flow

Login

↓

Hospital List

↓

Read every row

↓

Check image src

↓

if src == hospital.jpg

↓

Process

else

↓

Skip

↓

Open Edit

↓

Upload image

↓

Submit popup

↓

Submit page

↓

Next hospital

↓

Next page

---

# Future Improvements

Version 2

Separate Image Downloader

Hospital Name

↓

Search

↓

Official website

↓

Download image

↓

Save locally

Version 3

Uploader reads local folder only.

Version 4

Downloader + Uploader integrated.

Version 5

Professional GUI.

---

# Notes

This project is intended to become a reusable automation framework.

The architecture should remain generic so it can later automate:

- Hospitals
- Schools
- Hotels
- Restaurants
- Clinics
- Product catalogs

Only the image source and selectors should change.

---

# Current Status

Environment
✅ Complete

Login
✅ Complete

Navigation
✅ Complete

Hospital List
✅ Complete

Placeholder Detection
✅ Complete

Uploader
🟡 In Progress

Downloader
🔴 Pending

Logging
🔴 Pending

Pagination
🔴 Pending

GUI
🔴 Pending