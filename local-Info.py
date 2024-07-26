import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://example.com/local-news'

# Send a request to fetch the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the relevant content (e.g., news headlines)
headlines = soup.find_all('h2', class_='headline')

# Extract and print the headlines
for headline in headlines:
    print(headline.text.strip())
