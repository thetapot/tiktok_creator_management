import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def set_follower_count(driver, min_count, max_count):
    # Clear and set the minimum follower count
    try:
        min_count_input = driver.find_element(By.XPATH, "//input[@value='0']")
        min_count_input.click()
        for _ in range(10):
            min_count_input.send_keys(Keys.BACKSPACE)  # Clear the field by hitting delete/backspace key
        min_count_input.send_keys(str(min_count))
        print(f"Set min_count to {min_count}")
    except Exception as e:
        print("Error: Could not find or set the min_count input field.")
        print(str(e))
        return False

    # Clear and set the maximum follower count
    try:
        max_count_input = driver.find_element(By.XPATH, "//input[@value='10,000,000+']")
        max_count_input.click()
        for _ in range(10):
            max_count_input.send_keys(Keys.BACKSPACE)  # Clear the field by hitting delete/backspace key
        max_count_input.send_keys(str(max_count))
        print(f"Set max_count to {max_count}")
    except Exception as e:
        print("Error: Could not find or set the max_count input field.")
        print(str(e))
        return False

    return True


def add_creators_to_manage(driver, min_count, max_count):
    # Wait for the page to load completely
    time.sleep(5)

    # Click on the "Creators" button
    try:
        creators_button = driver.find_element(By.XPATH, "//button[span='Creators']")
        creators_button.click()
        print("Clicked on 'Creators' button.")
        time.sleep(2)  # Wait for the next elements to load
    except Exception as e:
        print("Error: Could not find the 'Creators' button.")
        print(str(e))
        return

    # Click on the "Follower count" option
    try:
        follower_count_div = driver.find_element(By.XPATH, "//div[contains(text(), 'Follower count')]")
        follower_count_div.click()
        print("Clicked on 'Follower count'.")
        time.sleep(2)  # Wait for the page to refresh or apply the filter
    except Exception as e:
        print("Error: Could not find the 'Follower count' option.")
        print(str(e))
        return

    # Set the min_count and max_count values
    if not set_follower_count(driver, min_count, max_count):
        return

    # Start time tracking for the 15-minute duration
    start_time = time.time()
    duration = 15 * 60  # 15 minutes in seconds

    while time.time() - start_time < duration:
        # Press space key 10 times to scroll down and load more creators
        for _ in range(10):
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SPACE)
            print("Pressed space key to scroll down.")
            time.sleep(1)  # Small delay between key presses

        # Wait for the content to load
        time.sleep(10)  # Pause for 10 seconds

        # Find creator rows and add them to "Manage Creators"
        creator_rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'cursor-pointer')]")

        for row in creator_rows:
            try:
                # Look for the "Add to Manage Creators" button in the row
                add_button = row.find_element(By.XPATH, ".//button[contains(@class, 'arco-btn-secondary')]")
                if add_button.is_enabled():
                    add_button.click()
                    print("Added a creator to Manage Creators.")
                    time.sleep(1)  # Brief pause after each click
            except Exception as e:
                print("Could not add creator from this row.")
                print(str(e))

    print("Finished scrolling and adding creators.")