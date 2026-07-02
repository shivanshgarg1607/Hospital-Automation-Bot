from admin import AdminBot


def main():

    bot = AdminBot()

    try:

        bot.launch_browser()

        bot.login()

        bot.open_hospital_page()

        hospital = bot.find_first_placeholder_hospital()

        if hospital:

            print("=" * 60)
            print("Hospital Found")
            print("=" * 60)
            print(f"Name      : {hospital['name']}")
            print(f"Image     : {hospital['image_src']}")
            print(f"Edit URL  : {hospital['edit_url']}")

            bot.open_edit_page(hospital)

            bot.open_choose_image_modal()

            success = bot.upload_image()

            if success:
                print("\n✅ Upload completed.")
            else:
                print("\n❌ Upload failed.")

        else:

            print("No hospitals require processing.")

        input("\nPress ENTER to close...")

    finally:
        bot.close()


if __name__ == "__main__":
    main()