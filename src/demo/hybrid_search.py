from langchain_community.document_loaders.pdf import PyPDFium2Loader
from demo.vdb import get_hybrid_db_connection
import os
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings

load_dotenv(override=True)


embedding = CohereEmbeddings(model="embed-english-light-v3.0")


path_to_file = "Garfield.pdf"

# Load the PDF file.
docs = PyPDFium2Loader(file_path=path_to_file).load()

# load the vdb
mongo_db = get_hybrid_db_connection(embedding=embedding)

# Upload the documents to the vector store.



