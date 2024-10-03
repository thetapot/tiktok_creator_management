from open_site import open_tiktok_affiliate_site, open_and_wait_for_user_close
from add_creators import add_creators_to_manage


def main():
    # Call the function to open the browser and wait for the user to close it
    open_and_wait_for_user_close()

    # List of follower count ranges
    follower_ranges = [
        (5000, 6000),
        (6000, 7000),
        (7000, 8000),
        (8000, 9000),
        (9000, 10000)
    ]

    # Loop through each range
    for min_count, max_count in follower_ranges:
        print(f"Processing follower count range: {min_count}-{max_count}")

        # Open the website with the Chrome driver
        driver = open_tiktok_affiliate_site()

        # Perform the add creators process with the current range
        add_creators_to_manage(driver, min_count, max_count)

        # Close the Chrome driver
        driver.quit()

        print(f"Finished processing follower count range: {min_count}-{max_count}\n")


if __name__ == "__main__":
    main()