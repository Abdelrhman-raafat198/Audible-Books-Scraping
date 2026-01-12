Audible Web Scraper 🎧
​This is a Python-based web scraping project that extracts audiobook data from Audible. The script navigates through multiple pages, collects key information about books, and saves the final dataset into an Excel file.
​✨ Features
​Multi-page Scraping: Automatically iterates through 25 pages of search results.
​Data Points Extracted: * Book Title.
​Author Name.
​Runtime (Duration).
​Rating.
​Price.
​Headless Support: Includes an option to run the browser in the background for faster performance.
​Error Handling: Robust try-except blocks to ensure the scraper doesn't crash during navigation.
​🛠️ Tech Stack
​Python
​Selenium: For web automation and dynamic content handling.
​Pandas: For data organization and exporting to Excel.
​Chrome WebDriver Manager: Automatically manages the driver version.

📂 Output
​The script generates an Excel file named Audible_data.xlsx (or your custom path) containing all the scraped records in a structured format.
##Sample Results
![Audible Data Results](results.png)
