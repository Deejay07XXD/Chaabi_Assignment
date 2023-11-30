# Chaabi_Assignment
This is my submission for chaabi campus placement at IITD
## Overview
This project is a semantic search engine designed to leverage advanced NLP techniques and vector search capabilities. Using Word2Vec for vectorizing text data and Qdrant for efficient vector search, It offers a powerful platform for performing semantic searches in large datasets.
##Implement vector embeddings on the given dataset and store them in a Vector DB
like Qdrant.-I implemented embeddings using word2vec which was used for search querry in MainNotebook.impyb
##Implement an LLM on the DB that can give contextual answers to the queries
strictly from the database.-Used Bert transformer in bert.impyb file which uses bert to generate embedding instead of word2vec to capture semantic information
##Wrap this LLM as an API using any framework.-used a simple flask api to wrap up word2vec searcher bert searcher can also be used similarly

