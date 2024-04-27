from Google_Search import *
from Fetch_Page import *
from De_duplicate import *

def main():
    query = input("Enter your search query: ")
    # num_results = int(input("Enter the number of search results to fetch: "))
    while True:
        try:
            num_results = int(input("Enter the number of search results to fetch: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            num_depth = int(input("Enter the number of depth for scraping: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    visitedSite.clear()
    links = [(i,num_depth) for i in scrape_google_search(query,num_results)]
    collection = []

    for (link, depth) in links:
        try:
            paragraphs, pagelinks = fetchPage(link, depth)
        except Exception as e:
            continue
        collection.append(paragraphs)
        if pagelinks != None:
            for i in pagelinks:
                links.append((i,depth-1))
    print(len(collection))

    with open('Mark search.txt', 'w', encoding='utf-8') as f:
        for item in collection:
            f.write(str(item) + '\n')


if __name__ == "__main__":
    main()
