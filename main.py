import os
import pickle
import streamlit as st
from dotenv import load_dotenv

from langchain.document_loaders import SeleniumURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOllama
from langchain_community.llms import HuggingFaceHub

# Load environment variables
load_dotenv()

# Streamlit UI
st.title("📰 News Research Tool")
st.sidebar.title("🔗 News Article Links")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}").strip().strip("'").strip('"')
    if url:
        urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
filepath = "faiss_store.pkl"
main_placefolder = st.empty()



from langchain_groq import ChatGroq  # ✅ Official LangChain integration

# Load Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("groq_api_key"),
    model="llama3-8b-8192"  # or "llama3-70b-8192", "mixtral-8x7b-32768"
)

if process_url_clicked and urls:
    try:
        # Load data from URLs
        loader = SeleniumURLLoader(urls=urls)
        main_placefolder.text("🔄 Loading data from URLs...")
        data = loader.load()

        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        main_placefolder.text("✂️ Splitting text into chunks...")
        docs = splitter.split_documents(data)

        if not docs:
            st.error("⚠️ No content extracted from the provided URLs.")
        else:
            # Create embeddings and FAISS index
            main_placefolder.text("🧠 Generating embeddings and building FAISS index...")
            embeddings = HuggingFaceEmbeddings()
            vectorstore = FAISS.from_documents(docs, embeddings)

            # Save index to disk
            with open(filepath, "wb") as f:
                pickle.dump(vectorstore, f)

            st.success("✅ URL content processed and indexed.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# Ask a question
query = main_placefolder.text_input("❓ Ask a question:")
if query:
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            vectorstore = pickle.load(f)

        # Create conversational retrieval chain
        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            return_source_documents=True
        )

        # Query without chat history for now
        result = chain({"question": query, "chat_history": []})

        st.header("🧾 Answer")
        st.subheader(result["answer"])

        if result.get("source_documents"):
            st.subheader("🔍 Sources:")
            for doc in result["source_documents"]:
                st.write(doc.metadata.get("source", ""))
    else:
        st.warning("⚠️ Please process the URLs first.")
