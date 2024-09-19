import streamlit as st
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import CohereEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.llms.cohere import Cohere
from langchain.chains.question_answering import load_qa_chain

st.header("My new RAG  AI")

with st.sidebar:
    st.title("Upload your PDF")
    file = st.file_uploader("Place your PDF here")

COHERE_API_KEY = "openai key"

if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len
    )

    chunks = text_splitter.split_text(text)

    embeddings = CohereEmbeddings(cohere_api_key=COHERE_API_KEY)
    vector_storage = FAISS.from_texts(chunks, embeddings)

    user_question = st.text_input("Type your question")

    if user_question:
        match = vector_storage.similarity_search(user_question)

        llm = Cohere(
            cohere_api_key=COHERE_API_KEY,
            model="medium",
            temperature=0.0,
            max_tokens=100
        )

        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=match, question=user_question)

        st.write(response)
