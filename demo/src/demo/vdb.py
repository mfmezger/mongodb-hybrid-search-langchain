import os

from dotenv import load_dotenv
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_mongodb.retrievers import MongoDBAtlasHybridSearchRetriever
from pymongo import MongoClient

load_dotenv(override=True)

# Create the vector store connection with MONGODB Atlas.
embedding = 
client: MongoClient = MongoClient(os.getenv("MONGODB_ATLAS_CLUSTER_URI"))

collection = client[os.getenv("DB_NAME", "")][os.getenv("COLLECTION_NAME", "")]

vector_db = MongoDBAtlasVectorSearch(
    collection=collection,
    embedding=embedding,
    index_name=os.getenv("VECTOR_SEARCH_INDEX_NAME", ""),
)

post_filter_pipeline = [
    {
        "$project": {
            "title": 0,
        }
    }
]


hybrid_db = MongoDBAtlasHybridSearchRetriever(
    vectorstore=vector_db,
    search_index_name=os.getenv("FULL_TEXT_SEACH_INDEX_NAME", ""),
    top_k=os.getenv("AMOUNT_OF_SEARCH_RESULTS", "40"),
    post_filter=post_filter_pipeline,
)

