"""Example for Hybrid Search."""

from typing import TYPE_CHECKING

from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings
from loguru import logger

from demo.vdb import get_hybrid_db_connection

if TYPE_CHECKING:
    from langchain_mongodb.retrievers import MongoDBAtlasHybridSearchRetriever

load_dotenv(override=True)


def main() -> None:
    """Example of how to retrieve with MongoDBHybrid search."""
    # load the vdb
    embedding = CohereEmbeddings(model="embed-english-light-v3.0")
    mongo_db: MongoDBAtlasHybridSearchRetriever = get_hybrid_db_connection(embedding=embedding)

    results = mongo_db.invoke({"Who inventend Garfield?"})

    logger.info(results)


if __name__ == "__main__":
    main()
