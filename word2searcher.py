from gensim.models import Word2Vec
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from qdrant_client import models
import pandas as pd

def average_vector(description, model):
    vectors = [model.wv[word] for word in description if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)
class Word2VecSearcher:
    def __init__(self, collection_name, word2vec_model_path):
        self.collection_name = collection_name
        self.model = Word2Vec.load(word2vec_model_path)
        self.qdrant_client = QdrantClient(host='localhost', port=6333)

    def search(self, query_text, top_k=5):
        # Tokenize and encode the query text into a vector

        query_tokens = query_text.lower().split()
        #query_vector = [self.model.wv[word] for word in query_tokens if word in self.model.wv]
        query_vector=average_vector(query_tokens, self.model)

        if  len(query_vector)==0:
            return []  # Return empty if no words are found in the model
        #query_vector = np.mean(query_vector, axis=0).tolist()

        # Perform the search
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            query_filter=None,  # Add filters if needed
            limit=top_k
        )

        # Extract results
        return [hit.payload for hit in search_result]
