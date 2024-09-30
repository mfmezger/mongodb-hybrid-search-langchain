"""Upload Example."""

from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings
from langchain_community.document_loaders.pdf import PyPDFium2Loader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from demo.vdb import connect_to_mongodb

# loading the environment variables.
load_dotenv(override=True)

# Path to the PDF file.
path_to_file = "Garfield.pdf"


def main() -> None:
    """Embedding Data."""
    # text splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20, length_function=len, separators=["\n\n", "\n", " ", "."])

    # Embedding model
    embedding = CohereEmbeddings(model="embed-english-light-v3.0")

    # Load the PDF file and then split the text into chunks.
    docs = PyPDFium2Loader(file_path=path_to_file).load_and_split(text_splitter)

    # load the vdb
    mongo_db = connect_to_mongodb(embedding=embedding)

    # Upload the documents to the vector store.
    mongo_db.add_documents(docs)


if __name__ == "__main__":
    main()
