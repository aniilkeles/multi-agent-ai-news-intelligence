from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.IndexFlatL2(384)

documents = []

def add_memory(text):

    embedding = model.encode([text])

    index.add(np.array(embedding))

    documents.append(text)

def search_memory(query):

    if len(documents) == 0:
        return []

    embedding = model.encode([query])

    k = min(2, len(documents))

    D, I = index.search(np.array(embedding), k=k)

    results = []

    for idx in I[0]:
        if idx < len(documents):
            results.append(documents[idx])

    return results