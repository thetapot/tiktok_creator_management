TikTok Creator Scraper

This project automates the process of scraping TikTok creators from the TikTok Affiliate website based on follower count ranges. It interacts with the website through Selenium WebDriver, automating browser actions such as filtering by follower count, scrolling, and adding creators to a management list.

Features

	•	Automates interaction with the TikTok Affiliate website.
	•	Filters creators based on a specified range of follower counts.
	•	Handles browser window closures gracefully and continues to the next follower count range.
	•	Supports the addition of creators to a “Manage Creators” list.
	•	Supports browser actions such as scrolling and element clicking.
	•	Error handling for common Selenium exceptions.

Requirements

	•	Python 3.8+
	•	Selenium WebDriver
	•	ChromeDriver (for controlling Google Chrome)
	•	Google Chrome installed

Python Packages

The following Python packages are required:

	•	selenium

You can install these packages using pip:

pip install selenium

ChromeDriver

Make sure you have ChromeDriver installed and added to your system’s PATH. You can download it from here.

Setup

 1. Clone the repository:
   git clone https://github.com/your-username/tiktok_add_creators.git
   cd tiktok_add_creators
	2.	Install the required Python packages:
   pip install -r requirements.txt
  3.	Download and install the correct version of ChromeDriver for your Chrome browser, and ensure it’s accessible in your system’s PATH.
	4.	Update the chromedriver_path in the code if necessary to point to your local ChromeDriver.

Usage

Running the Scraper

The main script is main.py, which starts the process of filtering creators by follower count and adding them to the “Manage Creators” list.
python main.py
Workflow

	1.	Browser Launch: The script opens a browser window and navigates to the TikTok Affiliate website. The script pauses until the user manually closes the browser.
	2.	Filtering Creators: After the browser is closed, the script proceeds with filtering creators based on follower count ranges. The user can specify follower ranges.
	3.	Scroll and Add Creators: The script scrolls through the creator list and attempts to add each creator to the “Manage Creators” list.
	4.	Error Handling: If any errors or browser closures occur during execution, the script will handle them gracefully and proceed with the next follower count range.
	5.	Follower Ranges: The script loops through different follower count ranges, such as 5000-6000, 6000-7000, etc., and performs the actions for each range.

Customizing Follower Count Ranges

You can customize the follower count ranges by modifying the list in the main.py file:
```
follower_ranges = [
    (5000, 6000),
    (6000, 7000),
    (7000, 8000),
    (8000, 9000),
    (9000, 10000)
]
```
