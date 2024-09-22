from langchain_community.document_loaders.pdf import PyPDFium2Loader


path_to_file = "Garfield.pdf"

# Load the PDF file.
docs = PyPDFium2Loader(file_path=path_to_file).load()