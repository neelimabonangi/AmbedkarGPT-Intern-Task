# ⭐ Ambedkar RAG Q&A System

A simple and powerful **offline Question–Answering system** that answers questions about **Dr. B. R. Ambedkar** using your local computer — no API key, no internet required.

This project uses:

- **LangChain**
- **ChromaDB**
- **HuggingFace Embeddings**
- **Ollama (llama3.2:1b model)**
- **Python 3.11**

It loads text from `ambedkar.txt`, creates embeddings, stores them in ChromaDB, retrieves relevant content based on your question, and generates an answer using a local LLM (Ollama).

---

## 🚀 Features

- 🔌 **100% Offline** — Works without internet or API keys  
- ⚡ **Fast Search** using Chroma Vector Database  
- 🤖 **Local LLM** using Ollama (llama3.2:1b)  
- 📄 **Easy to Update** — Just replace `ambedkar.txt`  
- 🧠 **Accurate Answers** using Retrieval-Augmented Generation (RAG)  

---


---

## 🧩 Installation steps

Follow these steps carefully.

---

## 1. Create Project Folder

Create a folder anywhere on your system:

```
ambedkar-rag-qna/
```

Put these files inside:

- `main.py`
- `ambedkar.txt`
- `requirements.txt`

---

## 2. Create Virtual Environment

Open **VS Code** → Open this project folder → Open terminal and run:

```bash
python -m venv env
```

Activate it:

### Windows:
```bash
env\Scripts\activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download Ollama from:  
👉 https://ollama.com/download

After installation, pull the required model:

```bash
ollama pull llama3.2:1b
```

(You can also use `llama3:latest` if you prefer.)

---

## 5. Run the Application

```bash
python main.py
```

You will see:

```
Ready! Ask questions about Ambedkar.
Ask:
```

Now type:

```
What is the main message of Ambedkar's speech?
```

---

## 💡 Example Questions to Try

```
What did Ambedkar say about hero worship?
When was he born?
Give a summary of the text.
What warnings did he give in the speech?
```

---

## 🧠 How RAG Works (Simple Explanation)

1. Load text from `ambedkar.txt`  
2. Split text into chunks  
3. Convert chunks → embeddings  
4. Store embeddings inside ChromaDB  
5. When user asks a question → retrieve matching chunks  
6. Pass retrieved text + question → LLM  
7. LLM generates accurate answer based on context  

---

## 🎯 Benefits of This Project

- Learn RAG (Retrieval Augmented Generation)
- Practice LangChain + ChromaDB
- Use offline LLM with Ollama
- Build your own Q&A assistant on any topic

---

## 📝 Notes

- Telemetry is disabled for privacy  
- Ensure `ambedkar.txt` contains proper readable text  
- Avoid large models if system RAM is low  

---






