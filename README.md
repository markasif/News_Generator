# 📰 News_Research_Tool – LangChain + ChatGroq + Streamlit

## 📘 Overview  
**News Research Tool** is a Streamlit-based web application that allows users to analyze and interact with content from multiple news articles using Large Language Models (LLMs). Simply paste article URLs, and the app extracts, processes, and semantically searches the content, allowing users to ask questions and receive intelligent, contextual answers. It leverages the power of **LangChain**, **FAISS**, **HuggingFace embeddings**, and **ChatGroq** APIs—without requiring any local model downloads.

---

## 🚀 Features

- 🔗 Accepts up to 3 article URLs  
- 🕷 Scrapes and processes content using Selenium  
- ✂️ Splits articles into semantic chunks  
- 🧠 Generates sentence embeddings using HuggingFace  
- 💾 Stores and retrieves using FAISS vector index  
- 💬 Enables natural language Q&A with context  
- 📚 Returns cited sources for every response  
- ⚡ Powered by Groq’s ultra-fast hosted LLMs  

---

## 💡 Use Cases

- Summarize and compare multiple articles  
- Journalistic research and media bias analysis  
- Academic reference extraction  
- Competitive and political content insights  
- Quick Q&A from large articles  

---

## 🛠 Tech Stack

| Tool                     | Purpose                           |
|--------------------------|-----------------------------------|
| **Streamlit**            | Web interface                     |
| **LangChain**            | LLM orchestration framework       |
| **ChatGroq**             | Hosted LLM backend                |
| **HuggingFace**          | Text embedding generation         |
| **FAISS**                | Semantic vector search            |
| **Selenium**             | Article content scraping          |

---

## 📂 How to Use

### ✅ How to run the project

- Create a new conda environment using `conda create -n news_env python=3.10` and activate it using `conda activate news_env`.
- Install all dependencies by running:  
  ```bash
  pip install -r requirements.txt
- Create a .env file and paste Your Api_key of Groq.
- Run streamlit application by running:
```bash
  streamlit run python main.py
```
## 📸 Output

Below are sample screenshots of the News Research Tool in action:

### 🖼 Interface with User Query

![News Generator Screenshot 1](screenshots/news_generator1.png)

### 🧠 Generated Answer with Source

![News Generator Screenshot 2](screenshots/news_generator2.png)
