import streamlit as st
# import faiss
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.cohere import CohereEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatCohere

st.header("My new RAG")
#
with st.sidebar:
    st.title("Upload your pdf")
    file = st.file_uploader("place your pdf here")
#
COHERE_API_KEY = "jLgQC4J7TVwRewB77c5hKi3mrb0C8HhAcnLowOP5"
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


    embeddings = CohereEmbeddings(cohere_api_key=COHERE_API_KEY,user_agent="your_app_name")

    embedding = embeddings.embed_documents(chunk)

    vector_storage = FAISS.from_texts(chunk, embeddings)

    user_question = st.file_uploader("type your questions")

    if user_question:
        match = vector_storage.similarity_search(user_question)
        # st.write(match)

        llm = ChatCohere(
            cohere_api_key=COHERE_API_KEY,
            temperature=0,
            max_token=100,
            model_name="cohere"
        )

        chain = load_qa_chain(llm, chain_type="stuff")
        respon = chain.run(input_document=match, question=user_question)
        st.write(respon)














