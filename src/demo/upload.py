from langchain_community.document_loaders.pdf import PyPDFium2Loader
from demo.vdb import connect_to_mongodb
import os
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv(override=True)

# text splitter
text_splitter = RecursiveCharacterTextSplitter(    chunk_size=500,
    chunk_overlap=20,
    length_function=len,
    separators=[
        "\n\n",
        "\n",
        " ",
        ".",])

embedding = CohereEmbeddings(model="embed-english-light-v3.0")


path_to_file = "Garfield.pdf"

# Load the PDF file and then split the text into chunks.
docs = PyPDFium2Loader(file_path=path_to_file).load_and_split(text_splitter)

# load the vdb
mongo_db = connect_to_mongodb(embedding=embedding)

# Upload the documents to the vector store.
mongo_db.add_documents(docs)



