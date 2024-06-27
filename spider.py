import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin 

visited_urls = set()

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Error: Request failed {url}") 
        return
    
    if response.status_code == 200 :
        soup = BeautifulSoup(response.content, 'html.parser')
        
        a_tag = soup.find_all("a")
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        # print(urls)
        for url2 in urls:
            if url2 not in visited_urls:
                visited_urls.add(url2)
                url_join = urljoin(url, url2)
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join, keyword)
            else:
                pass

url = input("Target url to scrape: ")

keyword = input("Keyword to search for in the URL provided: ")

spider_urls(url, keyword)
