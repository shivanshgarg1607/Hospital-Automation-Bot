from admin import AdminBot


def main():

    bot = AdminBot()

    try:

        bot.launch_browser()

        bot.login()

        bot.open_hospital_page()

        while True:

            hospital = bot.find_first_placeholder_hospital()

            if hospital:

                print("\n" + "=" * 60)
                print("Hospital Found")
                print("=" * 60)

                print(f"Name : {hospital['name']}")
                print(f"Image: {hospital['image_src']}")

                bot.open_edit_page(hospital)

                bot.open_choose_image_modal()

                success = bot.upload_image(hospital)

                if success:

                    print("\n✅ Image uploaded.")

                    bot.submit_hospital()

                    print("\nReturning to hospital list...")

                    bot.open_hospital_page()

                    continue

            print("\nNo placeholder hospitals on this page.")

            if bot.go_to_next_page():

                continue

            print("\n" + "=" * 60)
            print("ALL PAGES COMPLETED")
            print("=" * 60)

            break

    finally:

        input("\nPress ENTER to close...")

        bot.close()


if __name__ == "__main__":
    main()