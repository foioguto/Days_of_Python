import requests
from bs4 import BeautifulSoup

class Engine:
    def __init__(self, date, header, URL):
        self.date = date
        self.header = header
        self.url = url

    def __str__(self):
        return f"{self.date}"
    
    def travel(self):
        response = requests.get(self.URL, self.header)
        website_html = response.text

        soup = BeautifulSoup(website_html, "html.parser")
        print(soup.prettify())

