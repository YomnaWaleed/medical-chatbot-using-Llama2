from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


#Extract data from pdf
def load_pdf(data):
  loader = DirectoryLoader(data,
                           glob = "*.pdf",
                           loader_cls=PyPDFLoader)
  documents = loader.load()
  return documents



# create text chunks
def text_split(extracted_data):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20 )
  text_chunks = text_splitter.split_documents(extracted_data)
  return text_chunks
  


# download embedding model
def download_hugging_face_embeddings():
  embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
  return embedding


def store_data_in_faiss(text_chunks, embeddings):
    vectorstore = FAISS.from_documents(
        documents=text_chunks,
        embedding=embeddings
    )
    vectorstore.save_local("faiss_index")  # Save the index locally
    return vectorstore