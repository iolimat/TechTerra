import tiktoken

def chunk_text(text, max_tokens=2048):
    """Chunk the text into a list of strings based on the maximum number of tokens"""
    encoding = tiktoken.get_encoding("cl100k_base")

    chunks = []
    current_chunk = ""
    for token in encoding.encode(text):
        current_chunk += encoding.decode([token])
        if len(encoding.encode(current_chunk)) > max_tokens:
            chunks.append(current_chunk.strip())
            current_chunk = ""

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks