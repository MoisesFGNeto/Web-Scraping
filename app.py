"""
Second approach to scrapes book titles from 'books.toscrape.com' that have a 2-star rating.
"""
import requests
from bs4 import BeautifulSoup

# Constants
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

two_star_title = []

for n in range(1,51):
    scrape_url = BASE_URL.format(n)
    res = requests.get(scrape_url,timeout=5)
    soup = BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_title.append(book.select('a')[1]['title'])

print(two_star_title)
