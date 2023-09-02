# Web Scraping with Flask, Selenium, and BeautifulSoup

This project demonstrates web scraping using Python, Flask, Selenium, and BeautifulSoup (bs4) to collect job listings from a website and display them on a local web page.

## Installation

1. Install Flask:

- pip install flask

2. Install Selenium:

- pip install selenium

3. Install BeautifulSoup (bs4):

- pip install bs4

4. Install Chrome WebDriver (if not already installed):

- Download the Chrome WebDriver that matches your Chrome version: https://sites.google.com/chromium.org/driver/
- Place the WebDriver executable in a directory included in your system's PATH.

## Usage

1. Run the Flask application:

- python your_app.py

- Replace `your_app.py` with the name of your Python script.

2. Open your web browser and navigate to:

http://localhost:12345

- Replace `12345` with the port number specified in your Flask app.

3. You will see a web page displaying job listings scraped from the specified URL.

## How It Works

This project uses Flask to create a simple web server, Selenium for web automation, and BeautifulSoup for parsing HTML content. The Flask app serves a web page that displays job listings fetched from a specific URL.

### Project Structure

- `your_app.py`: The main Python script that configures the Flask app and performs web scraping.
- `templates/index.html`: The HTML template for displaying scraped job listings on the web page.

### Web Scraping Process

1. The Flask app starts and opens a web page using Selenium.
2. It retrieves the page source and parses it using BeautifulSoup.
3. The app extracts job listings' information (title, company, location, description) from the HTML.
4. Job information is stored in a list and displayed on the web page using the HTML template.

### Customize and Expand

You can customize this project to scrape data from other websites or add more features to the web page. Explore and modify the code to suit your specific web scraping needs.

Happy web scraping!

