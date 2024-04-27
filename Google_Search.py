import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import validators
import utils

def extract_top_links(urls, num_results):
    top_links = []
    for url in urls:
        if len(top_links) == num_results:
            break
        url = url['href']
        if url.startswith('/url?esrc=s&q=&rct=j&sa=U&url=https://'):
            # Extract the actual URL from the Google redirect URL
            if url.find('https://www.google.com') != -1 or url.find('http://www.google.com') != -1:
                continue
            start_index = url.find('url=') + len('url=')
            end_index = url.find('&', start_index)
            if end_index != -1:
                top_links.append(url[start_index:end_index])
    return top_links

def scrape_google_search(query, num_results):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    all_urls = []
    response = requests.get(url, headers=headers)
    # print(response.status_code)

    if response.status_code == 200:
        # Initialize BeautifulSoup with the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get all anchor tags (links) from the page
        links = soup.find_all('a', href=True)
        all_urls = extract_top_links(links, num_results)
    return all_urls