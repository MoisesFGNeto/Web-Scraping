"""
Web Scraping Script for Quotes to Scrape Website

This module provides tools to scrape quotes, authors, and tags from the website
'https://quotes.toscrape.com'. The script allows you to:

1. Scrape quotes, authors, and tags from individual pages.
2. Collect and print all quotes, authors, and tags from multiple pages.
3. Identify and list unique authors across multiple pages.

"""
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://quotes.toscrape.com/page/{}/'

def get_soup(url):
    '''
    Makes a request to the given URL and returns a BeautifulSoup object.
    '''
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')
        return soup
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def find_authors(soup):
    '''
    Find all elements with the class 'author'
    '''
    all_authors = set()
    authors = soup.findAll('small',class_='author')
    for author in authors:
        all_authors.add(author.text)
    print(all_authors)

    # -------- SECOND APROACH --------------
    #for name in soup.select(".author"):
    #all_authors.add(name.text)
    #print(all_authors)

def find_quotes(soup):
    '''
    Find all quotes
    '''
    all_quotes = []
    quotes = soup.findAll('span',class_='text')
    for quote in quotes:
        all_quotes.append(quote.text)
    print(all_quotes)

    # -------- SECOND APROACH --------------
    #for quote in soup.select(".text"):
    #   all_quotes.append(quote.text)
    # print(all_quotes)

def find_tags(soup):
    '''
    Find all Tags
    '''
    all_tags = []
    for tag in soup.select('.tag-item'):
        cleaned_tag = tag.text.strip()
        all_tags.append(cleaned_tag)
    print(all_tags)

def scrap_all_elemets_per_page():
    '''
    Scrap all quotes, authors and tags per page
    '''
    for page_num in range(1, 11):
        print(f"Scraping page {page_num}...")
        soup = get_soup(BASE_URL.format(page_num))
        find_quotes(soup)
        find_authors(soup)
        find_tags(soup)

def all_unique_authors_in_fixed_range_page():
    ''''
    Find all unique authors, knowing the quantity of pages
    '''
    unique_authors = set()
    for page in range(1,11):
        soup = get_soup(BASE_URL.format(page))
        if soup:
            for author in soup.select('.author'):
                unique_authors.add(author.text)
    print('Total of unique authors:', len(unique_authors))
    print('This is all unique authors: \n',unique_authors)

def all_unique_authors_in_unlimited_page():
    '''
    Find all unique authors, without knowing the quantity of pages
    '''
    page_still_valid = True
    unique_authors = set()
    page = 1

    while page_still_valid:
        soup = get_soup(BASE_URL.format(page))
        if "No quotes found!" in soup.text:
            break
        for name in soup.select('.author'):
            unique_authors.add(name.text)
        page += 1

    print('Total of unique authors:', len(unique_authors))
    print('This is all unique authors: \n',unique_authors)
