import requests
from bs4 import BeautifulSoup
from lxml import etree

url = "http://quotes.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

author_quotes = {}

for author_element, quote_element in zip(soup.select(".author"), soup.select(".text")):
    author = author_element.text
    quote = quote_element.text
    if author not in author_quotes:
        author_quotes[author] = []
    author_quotes[author].append(quote)

for page_number in range(2, 11):
    next_page_url = f"http://quotes.toscrape.com/page/{page_number}/"
    res = requests.get(next_page_url)
    soup = BeautifulSoup(res.text, 'lxml')

    for author_element, quote_element in zip(soup.select(".author"), soup.select(".text")):
        author = author_element.text
        quote = quote_element.text

        
        if author not in author_quotes:
            author_quotes[author] = []
        author_quotes[author].append(quote)

print("Quotes from ScrapingScript:")
for author, quotes in author_quotes.items():
    print(f"{author}")
    for quote in quotes:
        print(f"  - {quote}")