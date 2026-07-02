from pathlib import Path


def upload_image(page, image_path):

    image = Path(image_path)

    if not image.exists():

        print(f"\n❌ Image not found:\n{image}")

        return False

    print("\nOpening 'Add New Image' tab...")

    page.get_by_role(
        "link",
        name="Add New Image"
    ).click()

    page.wait_for_timeout(1000)

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