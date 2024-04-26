from googlesearch import search
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import validators

def is_valid_url(url):
    """
    Check if the URL is valid using the validators library.

    Args:
    url (str): The URL to validate.

    Returns:
    bool: True if the URL is valid, False otherwise.
    """
    return validators.url(url)

def get_top_search_results(query, num_results=10):
    """
    Perform a Google search and return top search results.

    Args:
    query (str): The search query.
    num_results (int): Number of search results to fetch.

    Returns:
    list: List of top search result URLs.
    """
    search_results = []
    try:
        # Perform the Google search
        search_query = search(query, num_results=num_results)
        # Iterate through the search results
        for result in search_query:
            search_results.append(result)
    except Exception as e:
        print(f"Error fetching search results: {e}")
    return search_results

def get_all_urls(base_url):
    """
    Extract all valid absolute URLs from a given base URL.

    Args:
    base_url (str): The base URL to extract URLs from.

    Returns:
    set: Set of valid absolute URLs found in the page.
    """
    all_urls = set()  # Initialize an empty set to store valid absolute URLs

    try:
        # Make a GET request to the base URL
        response = requests.get(base_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Initialize BeautifulSoup with the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get all anchor tags (links) from the page
            links = soup.find_all('a', href=True)
            
            # Extract and add valid absolute URLs to the set
            for link in links:
                href = link['href']
                absolute_url = urljoin(base_url, href)
                if is_valid_url(absolute_url):
                    all_urls.add(absolute_url)
        else:
            print(f"Failed to fetch URL: {base_url}")
    except Exception as e:
        print(f"Error fetching URL content: {e}")
    
    return all_urls

def main():
    query = input("Enter your search query: ")
    num_results = int(input("Enter the number of search results to fetch: "))
    urls = get_top_search_results(query, num_results)
    
    for url in urls:
        print(f"Extracted URLs from {url}:")
        extracted_urls = get_all_urls(url)
        for extracted_url in extracted_urls:
            print(extracted_url)

if __name__ == "__main__":
    main()