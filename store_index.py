from src.helper import load_pdf, text_split, download_hugging_face_embeddings, store_data_in_faiss
import os


extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)

embedding = download_hugging_face_embeddings()

vectorstore = store_data_in_faiss(text_chunks, embedding)