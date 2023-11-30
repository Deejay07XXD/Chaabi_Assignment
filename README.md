# Chaabi_Assignment
This is my submission for chaabi campus placement at IITD
## Overview
This project is a semantic search engine designed to leverage advanced NLP techniques and vector search capabilities. It presents the architecture for an appy through which a query can be made and the result ouputs most relevant products on basis of product, category, sub category, brand and description. 
In the model build process first the data is pre processed by filling the null values and the text in coverted into lower alphabets followed by tokenization of necessary parameters. 
Following this Word2Vec is used to vectorize the net field and generate a 100 sized embeddding.
These embeddings are stored in the embeddings.npy file which are acccessed whenever there is a query. Whenever a query is given by user the embedding is generated for that query and then cosine similarity is used to find similarity with database. This outputs the most relevant products with maximum similarity.

Qdrant database is used to upload the learning s that is embeddings of database on there database.
From the API Flask main code is app.py which processes the query and calls in word2searcher.py file where the match is found.

In the whole LLM models are used to generate embeddings and find semantic simimlarity between database and query.

Also, another architure is implemnted in bert.ipynb which implements BERT architecture to generate semantic embeddings which accounts the interconnection of words in a sentence and give bigger sized and better descriptive embedding. Rest architecture remains same.
Also mainnoitebook.ipynb file has rough code for word2vec.


##Steps
1. intsall requirement
pip install -r requirements.txt
2. run anaconda
conda create -n myenv python=3.8
conda activate myenv
jupyter notebook
3. run MainNotebook.
