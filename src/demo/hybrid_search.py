from demo.vdb import get_hybrid_db_connection
from langchain_mongodb.retrievers import MongoDBAtlasHybridSearchRetriever
from dotenv import load_dotenv
from loguru import logger
from langchain_cohere import CohereEmbeddings

load_dotenv(override=True)



def main():
    # load the vdb
    embedding = CohereEmbeddings(model="embed-english-light-v3.0")
    mongo_db: MongoDBAtlasHybridSearchRetriever = get_hybrid_db_connection(
        embedding=embedding
    )

    results = mongo_db.invoke({"Who inventend Garfield?"})

    logger.info(results)


if __name__ == "__main__":
    main()



