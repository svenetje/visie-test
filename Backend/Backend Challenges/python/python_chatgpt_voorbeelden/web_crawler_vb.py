import requests
from bs4 import BeautifulSoup

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        # print(href)
        if not href:
            continue
        if 'https://' not in href:
            href = f'{url}{href}'
        links.append(href)
        # print(links)
    return links

def web_crawler(seed_url):
    to_crawl = [seed_url]
    crawled = []
    while to_crawl:
        url = to_crawl.pop(0)
        if url not in crawled:
            print("Crawling:", url)
            links = get_links(url)
            to_crawl += links
            crawled.append(url)

web_crawler("https://visie-groep.nl")