import streamlit as st
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings  # Updated import
from langchain_community.vectorstores import FAISS  # Updated import
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI

st.header("My Chat Bot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file", type="pdf")

OPENAI_API_KEY = "your_openai_api_key_here"

if file is not None:
    # Read PDF and extract text
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    if text:
        st.write(text)

        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n"],
            chunk_size=1000,
            chunk_overlap=150,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        # Create embeddings and vector store
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        vector_store = FAISS.from_texts(chunks, embeddings)

        # User input for questions
        user_questions = st.text_input("Type your question here")

        if user_questions:
            # Search for similar text chunks
            match = vector_store.similarity_search(user_questions)

            # Load language model and QA chain
            llm = ChatOpenAI(
                openai_api_key=OPENAI_API_KEY,
                temperature=0,
                max_tokens=100,
                model_name="gpt-3.5-turbo"
            )

            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_document=match, questions=user_questions)
            st.write(response)
    else:
        st.write("No text extracted from the PDF.")
else:
    st.write("Please upload a PDF file.")
