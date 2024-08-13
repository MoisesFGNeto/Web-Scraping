"""
This module scrapes book titles from 'books.toscrape.com' that have a 2-star rating.
"""
import requests
from bs4 import BeautifulSoup

# Constants
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
TOTAL_PAGES = 50

def fetch_page(url):
    """
    Fetches the content of a page and handles errors.
    Args: url (str): The URL of the page to fetch.
    Returns: str: The HTML content of the page, or None if an error occurred.
    """
    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_page(content):
    """
    Parses the page content and extracts titles of 2-star books.
    Args: content (str): The HTML content of the page.
    Returns: list: A list of titles of books with a 2-star rating.
    """
    soup = BeautifulSoup(content, 'lxml')
    titles = []
    products = soup.select('.product_pod')
    for product in products:
        rating = product.find('p', class_='star-rating Two')
        if rating:
            title = product.h3.a['title']
            titles.append(title)
    return titles

def main():
    """
    Main function to scrape and display titles of 2-star books across multiple pages.
    """
    all_titles = []
    for page_num in range(1, TOTAL_PAGES + 1):
        url = BASE_URL.format(page_num)
        print(f"Scraping page {page_num}...")
        page_content = fetch_page(url)
        if page_content:
            titles = parse_page(page_content)
            all_titles.extend(titles)
    print(f"Found {len(all_titles)} books with a 2-star rating:")
    for title in all_titles:
        print(title)

if __name__ == "__main__":
    main()
