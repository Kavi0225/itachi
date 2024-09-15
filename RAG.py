import streamlit as st
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import cohere

st.header("My new RAG")

with st.sidebar:
    st.title("Upload your pdf")
    file = st.file_uploader("place your pdf here")

OPEN_AI_KEY = "EeQ1K2fvpfzNdjDlup5aCHkRGoN7krq81iKwzcVg"
if file is not None:
    Pdf_reader = PdfReader(file)
    text = ""
    for page in Pdf_reader.pages:
        text += page.extract_text()
        # st.write(text)

    text_spliter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len
    )

    chunk = text_spliter.split_text(text)

    embeddings = OpenAIEmbeddings(open_ai_key=OPEN_AI_KEY)

    vector_storage = FAISS.from_texts(chunk, embeddings)

    user_question = st.file_uploader("type your questions")

    if user_question:
        match = vector_storage.similarity_search(user_question)
        # st.write(match)

        llm = cohere(
            open_ai_key=OPEN_AI_KEY,
            temperature=0,
            max_token=100,
            model_name="cohere"
        )

        chain = load_qa_chain(llm, chain_type="stuff")
        respon = chain.run(input_document=match, question=user_question)
        st.write(respon)














