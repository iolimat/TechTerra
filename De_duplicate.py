from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_documents(documents):
    # Perform preprocessing steps such as tokenization, lowercasing, and stopword removal
    # Return preprocessed documents
    preprocessed_documents = []
    for doc in documents:
        # Perform your preprocessing steps here
        preprocessed_documents.append(doc.lower())  # Example: lowercase the document
    return preprocessed_documents


def check_similarty_between_two_collections(collection1, collection2, similarity_threshold=0.8):
    if not collection1 and not collection2:
        return []  # Handle empty input lists

    # Combine both collections
    all_docs = collection1 + collection2

    # Vectorize the documents using TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(all_docs)

    # Calculate cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix)

    # Determine which documents to keep
    keep_indices = set(range(len(all_docs)))  # Start with all indices

    # Remove indices of duplicates by comparing every pair of documents
    for i in range(len(all_docs)):
        for j in range(i + 1, len(all_docs)):
            if cosine_sim[i, j] > similarity_threshold and j in keep_indices:
                # Prefer to keep the first occurrence in the list
                keep_indices.remove(j)

    # Create a list of unique documents using the indices determined
    unique_documents = [all_docs[i] for i in sorted(keep_indices)]
    return unique_documents


# Example collections of documents
collection1 = [
    "This is document 1 in collection 1.",
    "This is document 2 in collection 1.",
    "This is document 3 in collection 1."
]

collection2 = [
    "This is document 1 in collection 2.",
    "This is document 2 in collection 2.",
    "This is document 3 in collection 2."
]

# Preprocess documents in both collections
preprocessed_collection1 = preprocess_documents(collection1)
preprocessed_collection2 = preprocess_documents(collection2)