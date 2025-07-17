from bs4 import BeautifulSoup
import requests
import csv



url = 'https://realpython.github.io/fake-jobs/'
response = requests.get(url)

# print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
div = soup.find_all("div",class_="column is-half")

# print("Job Titles:",div)

# ✅ Step 1: CSV file open karo aur headings likho
with open("jobs_data.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Job Title", "Company", "Location"])  # Header row

    # ✅ Step 2: Har job ka data file mein likho
    for job in div:
        title = job.find("h2", class_="title is-5")
        company = job.find("h3", class_="subtitle is-6 company")
        location = job.find("p", class_="location")
        
        if title and company and location:
            writer.writerow([
                title.text.strip(),
                company.text.strip(),
                location.text.strip()
            ])

print("✅ All job data saved to jobs_data.csv successfully!")