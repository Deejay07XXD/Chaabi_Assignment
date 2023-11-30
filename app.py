from flask import Flask, request, jsonify
from word2searcher import Word2VecSearcher  # Assuming Word2VecSearcher is in a separate file
import os
from qdrant_client import QdrantClient
app = Flask(__name__)

# Load the Word2Vec model and initialize the searcher
# Make sure to replace these with the correct values
COLLECTION_NAME = 'chaabi6'  # Name your collection
VECTOR_SIZE = 100  # This should match the vector_size used in Word2Vec
qdrant_client = QdrantClient(host = "localhost", port = 6333)

WORD2VEC_MODEL_PATH = "word2vec_bigbasket.model"
searcher = Word2VecSearcher(COLLECTION_NAME, WORD2VEC_MODEL_PATH)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    top_k = request.args.get('top_k', 5, type=int)
    results = searcher.search(query, top_k=top_k)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5001)))
