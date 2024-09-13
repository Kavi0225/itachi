import streamlit as st
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI
st.header("my chat bot")

with st.sidebar:
    st.title("your documents")
    file = st.file_uploader("upload a pdf file ", type="pdf")

OPENAI_API_KEY = ""
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        st.write(text)

    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    vector_store = FAISS.from_texts(chunks, embeddings)

    user_questions = st.text_input("type your question here")

    if user_questions:
        match = vector_store.similarity_search(user_questions)
        # st.write(match)

        llm = ChatOpenAI(
            openai_ai_key=OPENAI_API_KEY,
            temperature=0,
            max_token=100,
            model_name="gpt-3.5-turbo"
        )

        chain = load_qa_chain(llm, chain_type="stuff")
        respons = chain.run(input_document=match, questions=user_questions)
        st.write(respons)
