from flask import Flask, render_template
from bs4 import BeautifulSoup
from selenium import webdriver

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    url = "https://www.optioncarriere.tn/recherche/emplois?s=informatique&l=Tunisie&radius=15&sort=relevance"

    # Set up the Selenium driver
    driver = webdriver.Chrome()
    driver.get(url)

    # Get the page source and parse it with BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Find all job listings on the page
    job_listings = soup.find_all("article", class_="job clicky")

    # Create a list to store the job information
    jobs = []

    # Extract information for each job listing and store it in the jobs list
    for job in job_listings:
        title = job.find("header").get_text().strip()
        company = job.find("p", class_="company")
        location = job.find("ul", class_="location").get_text().strip()
        description = job.find("div", class_="desc").get_text().strip()

        jobs.append({
            'title': title,
            'company': company.get_text().strip() if company else "N/A",
            'location': location,
            'description': description
        })

    # Close the Selenium driver
    driver.quit()

    return render_template('index.html', jobs=jobs)

if __name__ == '__main__':
    app.run(port=12345,debug=True)
