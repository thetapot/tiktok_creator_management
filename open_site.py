from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

url = "https://affiliate-us.tiktok.com/connection/creator?shop_region=US"


def open_tiktok_affiliate_site():
    profile_path = "/Users/rero/Library/Application Support/Google/Chrome/Profile 35"
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={profile_path}")
    chrome_options.add_argument("--profile-directory=Profile 35")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    return driver


def open_and_wait_for_user_close():
    """Opens the browser and waits for the user to close the window."""
    profile_path = "/Users/rero/Library/Application Support/Google/Chrome/Profile 35"
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={profile_path}")
    chrome_options.add_argument("--profile-directory=Profile 35")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the URL
    print("Opening the browser. Close the browser window to continue.")
    driver.get(url)

    try:
        # Wait for the user to close the browser manually by checking if there are any open windows
        while len(driver.window_handles) > 0:
            time.sleep(1)  # Sleep for 1 second before checking again
    except Exception as e:
        print(f"An error occurred while waiting for the browser to close: {e}")
    finally:
        driver.quit()
        print("Browser closed by user. Continuing with the script.")