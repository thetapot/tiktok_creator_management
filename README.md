TikTok Creator Scraper
This project automates the process of scraping TikTok creators from the TikTok Affiliate website based on follower count ranges. It interacts with the website through Selenium WebDriver, automating browser actions such as filtering by follower count, scrolling, and adding creators to a management list.

Features
Automates interaction with the TikTok Affiliate website.
Filters creators based on a specified range of follower counts.
Handles browser window closures gracefully and continues to the next follower count range.
Supports the addition of creators to a "Manage Creators" list.
Supports browser actions such as scrolling and element clicking.
Error handling for common Selenium exceptions.
Requirements
Python 3.8+
Selenium WebDriver
ChromeDriver (for controlling Google Chrome)
Google Chrome installed
Python Packages
The following Python packages are required:

selenium
You can install these packages using pip:

bash
Copy code
pip install selenium
ChromeDriver
Make sure you have ChromeDriver installed and added to your system’s PATH. You can download it from here.

Setup
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/tiktok_add_creators.git
cd tiktok_add_creators
Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Download and install the correct version of ChromeDriver for your Chrome browser, and ensure it's accessible in your system's PATH.

Update the chromedriver_path in the code if necessary to point to your local ChromeDriver.

Usage
Running the Scraper
The main script is main.py, which starts the process of filtering creators by follower count and adding them to the "Manage Creators" list.

bash
Copy code
python main.py
Workflow
Browser Launch: The script opens a browser window and navigates to the TikTok Affiliate website. The script pauses until the user manually closes the browser.
Filtering Creators: After the browser is closed, the script proceeds with filtering creators based on follower count ranges. The user can specify follower ranges.
Scroll and Add Creators: The script scrolls through the creator list and attempts to add each creator to the "Manage Creators" list.
Error Handling: If any errors or browser closures occur during execution, the script will handle them gracefully and proceed with the next follower count range.
Follower Ranges: The script loops through different follower count ranges, such as 5000-6000, 6000-7000, etc., and performs the actions for each range.
Customizing Follower Count Ranges
You can customize the follower count ranges by modifying the list in the main.py file:

python
Copy code
follower_ranges = [
    (5000, 6000),
    (6000, 7000),
    (7000, 8000),
    (8000, 9000),
    (9000, 10000)
]
Handling Browser Closure
The script waits for the user to close the browser manually at the start, then proceeds with the automation. If the browser is closed unexpectedly during execution, the script will catch the exception and move on to the next follower count range.

Error Handling
The script has error handling for the following common exceptions:

WebDriverException: Catches issues related to the browser and WebDriver.
NoSuchElementException: Catches cases where elements (such as buttons) are not found on the page.
Graceful Browser Closure: If the browser is closed unexpectedly during execution, the script will move on to the next follower range.
Example Output
bash
Copy code
Processing follower count range: 5000-6000
Clicked on 'Creators' button.
Clicked on 'Follower count'.
Set min_count to 5000
Set max_count to 6000
Pressed space key to scroll down.
Added creator to Manage Creators.
...

Processing follower count range: 6000-7000
...
Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. Ensure that your code follows best practices and is well-documented.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Issues
If you encounter any issues, feel free to open an issue on GitHub.

