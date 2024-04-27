import requests
from bs4 import BeautifulSoup
import tldextract
import validators
from Filtter_document import  *

visitedSite = set()
def fetchPage(url, depth):
    # Send an HTTP GET request to the URL
    try:
        response = requests.get(url)
    except Exception as e:
        print("The error is: ", e)
        print("Couldn't access to the site")
        return
    if response.status_code == 200:
        extractURL = tldextract.extract(url)
        homePage = "www." + extractURL.subdomain + "." + extractURL.domain + "." + extractURL.suffix
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')

        paragraphs = []
        headers = []
        current_header = None
        links = []

        for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a' if depth > 0 else None]):
            if tag.name.startswith('h'):
                # If the tag is a header, update current_header
                current_header = tag.text.strip()
            elif tag.name == 'p':

                paragraph = tag.text
                paragraph = check_the_document(paragraph)
                if paragraph == "":
                    continue

                if current_header:
                    paragraphs.append(f"{current_header}: {paragraph}")
                else:
                    paragraphs.append(tag.text.strip())
            elif tag.name == 'a':
                lnk = tag.get('href')
                if validators.url(lnk):
                    if lnk not in visitedSite:
                        visitedSite.add(lnk)
                        links.append(lnk)
                elif lnk != "":
                    lnk = homePage + "/" + str(lnk)
                    if validators.url(lnk):
                        if lnk not in visitedSite:
                            visitedSite.add(lnk)
                            links.append(lnk)

        return paragraphs, links
    else:
        print("Failed to fetch webpage:", response.status_code)




#
# # Example URL
# url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
#
# # Fetch paragraphs and links from the webpage
# paragraphs, links = fetchPage(url, 1)
#
# # Print the paragraphs
# print("Paragraphs:")
# for paragraph in paragraphs:
#     print(paragraph)
#
# # Print the links
# print("\nLinks:")
# for link in links:
#     print(link)
