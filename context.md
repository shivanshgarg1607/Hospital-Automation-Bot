# Current Project Context

We have already completed:

✅ Python setup

✅ Playwright setup

✅ Login automation

✅ Navigation automation

✅ Hospital list access

✅ Reading hospital rows

Important discoveries:

1.

Missing hospital images always use

hospital.jpg

Example

https://karunahealthlifepartner.com/uploads/hospital.jpg

Therefore

if src.endswith("hospital.jpg")

↓

Hospital requires processing.

2.

Hospitals with real images should always be skipped.

3.

Pagination URLs are

/categoryitemSetting/1

/categoryitemSetting/1/10

/categoryitemSetting/1/20

The last number appears to be the offset.

4.

Upload workflow

Hospital List

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

Returns automatically to Hospital List

5.

The project should be written as production-quality software.

6.

Current objective

Finish the uploader first.

Downloader comes later.

7.

The user wants complete files rather than snippets during MVP development.

8.

After the MVP is complete the project should switch into learning mode where every concept is explained.