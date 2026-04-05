# 🧠 Swiggy RAG QA System (Offline AI)

A **Retrieval-Augmented Generation (RAG)** based AI system that answers user queries **strictly from the Swiggy Annual Report**.

This project demonstrates how to build a **production-style, hallucination-resistant AI system** using:

* 📄 PDF document processing
* 🧠 Semantic search (ChromaDB)
* 🤖 Local LLM (Ollama – Mistral / LLaMA3)
* ⚡ Fully offline pipeline (no API dependency)

---

# 🎯 Objective

To design an AI system that:

✔ Answers questions based ONLY on the Swiggy Annual Report
✔ Avoids hallucinations
✔ Uses retrieval + generation pipeline
✔ Works completely offline

---

# 🏗️ Architecture
<img src="https://raw.githubusercontent.com/Vithika2005/RAG_swiggy_ollama/main/rag_working.jpeg" width="800"/>
```
PDF → Text → Chunking → ChromaDB (Embeddings)
                                      ↓
User Query → Semantic Search → Context → Ollama → Answer
```

---

# 🧠 Key Concepts

### 🔹 Retrieval-Augmented Generation (RAG)

Instead of generating answers blindly, the system:

1. Retrieves relevant document chunks
2. Feeds them to the LLM
3. Generates grounded answers

---

### 🔹 Embeddings

Text is converted into vectors representing meaning.
This allows **semantic similarity search** instead of keyword matching.

---

### 🔹 Vector Database (ChromaDB)

Stores document embeddings and enables fast retrieval of relevant content.

---

### 🔹 Local LLM (Ollama)

* Uses models like **Mistral / LLaMA3**
* Runs entirely on local machine
* No API cost or internet dependency

---

# 📂 Project Structure

```
swiggy-rag/
 ├── backend/
 │   ├── main.py
 │   ├── rag/
 │   │   ├── pdf_to_text.py
 │   │   ├── chunking.py
 │   │   ├── embed_store.py
 │   │   ├── rag_answer.py
 │   └── data/
 │       └── swiggy_report.pdf
 ├── requirements.txt
 └── README.md
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone the Repository

```
git clone https://github.com/Vithika2005/RAG_swiggy_ollama.git
cd RAG_swiggy_ollama/backend
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r ../requirements.txt
```

---

## 4️⃣ Install Ollama

Download and install Ollama from:

👉 https://ollama.com

---

## 5️⃣ Pull Required Models

```
ollama pull mistral
```

(Optional)

```
ollama pull llama3
```

---

## 6️⃣ Add Swiggy Annual Report

Place the PDF in:

```
backend/data/swiggy_report.pdf
```

---

# ▶️ Running the Application

## Step 1 — Ingest Document

```
python main.py
```

Select:

```
1 → Ingest PDF
```

This will:

* Extract text
* Chunk document
* Create embeddings
* Store in ChromaDB

---

## Step 2 — Start Chat

Run again:

```
python main.py
```

Select:

```
2 → Chat
```

---

## 💬 Example Queries

* What are Swiggy’s risks?
* What business segments does Swiggy operate in?
* Who are key investors?
* What financial performance is reported?

---

# 🧪 Features

✔ Fully offline RAG pipeline
✔ Semantic search using embeddings
✔ Local LLM via Ollama
✔ Context-grounded answers
✔ CLI-based interaction

---

# ⚠️ Limitations

* Response time depends on local hardware
* Retrieval quality depends on chunking and embeddings
* No UI (CLI-based)

---

# 🚀 Future Improvements

* Add source citations (page numbers)
* Improve embeddings (Ollama embedding models)
* Build web interface (FastAPI + React)
* Add streaming responses
* Hybrid search (keyword + semantic)

---

# 📌 Source Document

Swiggy Annual Report (latest available public version)

(Add your exact link here)

---

# 🧠 Interview Explanation (Short)

This project implements a Retrieval-Augmented Generation system where document content is embedded and stored in a vector database. User queries are converted into embeddings, matched against stored vectors using semantic similarity, and the retrieved context is passed to a local LLM (Ollama) to generate grounded responses, eliminating hallucinations.

---

# 👩‍💻 Author

Vithika Surve

---

# ⭐ If you found this useful, consider starring the repo!
