from googlesearch import search

def get_top_search_results(query, num_results=10):
    search_results = []
    try:
        # Perform the Google search
        search_query = search(query, num_results=10)
        # Iterate through the search results
        for result in search_query:
            search_results.append(result)
    except Exception as e:
        print(f"Error fetching search results: {e}")
    return search_results

# Example usage
query = "Python programming"
num_results = 5
top_results = get_top_search_results(query, num_results)

# Print the top search results
print(f"Top {num_results} search results for '{query}':")
for idx, result in enumerate(top_results, start=1):
    print(f"{idx}. {result}")