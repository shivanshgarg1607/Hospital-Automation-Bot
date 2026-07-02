from pathlib import Path

from config import TEST_IMAGE_FOLDER


def get_test_image():

    folder = Path(TEST_IMAGE_FOLDER)

    if not folder.exists():
        print(f"\n❌ Folder not found:\n{folder}")
        return None

    images = []

    for extension in ("*.jpg", "*.jpeg", "*.png", "*.webp"):
        images.extend(folder.glob(extension))

    if not images:
        print("\n❌ No images found.")
        return None

    images.sort()

    return images[0]


def upload_image(page):

    print("\nOpening 'Add New Image' tab...")

    page.get_by_role(
        "link",
        name="Add New Image"
    ).click()

    page.wait_for_timeout(1000)

    image = get_test_image()

    if image is None:
        return False

    print(f"\nSelected image:\n{image}")

    file_input = page.locator("input[type='file']")

    file_input.set_input_files(str(image))

    print("✓ File selected.")

    page.wait_for_timeout(1000)

    print("Clicking UPLOAD...")

    page.get_by_role(
    "button",
    name="UPLOAD",
    exact=True
    ).click()

    print("Waiting for upload...")

    page.wait_for_timeout(8000)

    print("✓ Upload finished.")

    return True