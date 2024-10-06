"""Vector Database Connection."""

import os

from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_mongodb.retrievers import MongoDBAtlasHybridSearchRetriever
from pymongo import MongoClient

load_dotenv(override=True)


def connect_to_mongodb(embedding: CohereEmbeddings) -> MongoDBAtlasVectorSearch:
    """Create a MongoDBAtlasHybridSearchRetriever.

    Returns
    -------
        MongoDBAtlasHybridSearchRetriever: Hybrid Search with MongoDB Atlas.

    """
    # Create the MongoDB connection.
    client: MongoClient = MongoClient(os.getenv("MONGODB_ATLAS_CLUSTER_URI"))
    collection = client[os.getenv("MONGODB_DB_NAME")][os.getenv("MONGODB_COLLECTION_NAME")]

    # Create the vector store connection with MONGODB Atlas.
    return MongoDBAtlasVectorSearch(
        collection=collection,
        embedding=embedding,
        index_name=os.getenv("VECTOR_SEARCH_INDEX_NAME"),
    )


def get_hybrid_db_connection(embedding: CohereEmbeddings) -> MongoDBAtlasHybridSearchRetriever:
    """_summary_.

    Args:
    ----
        embedding (CohereEmbeddings): _description_

    Returns:
    -------
        MongoDBAtlasHybridSearchRetriever: _description_

    """
    # Create the MongoDB connection.
    vector_db = connect_to_mongodb(embedding=embedding)

    # for filtering the results, e.g. removing unnecessary fields.
    post_filter_pipeline = [
        {
            "$project": {
                "title": 0,
            }
        }
    ]
    return MongoDBAtlasHybridSearchRetriever(
        vectorstore=vector_db,
        search_index_name=os.getenv("FULL_TEXT_SEACH_INDEX_NAME", ""),
        top_k=10,  # Number of documents to retrieve.
        post_filter=post_filter_pipeline,
    )
