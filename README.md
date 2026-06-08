# 📊 Statistics AI Tutor (RAG-Powered)

## Overview

Statistics AI Tutor is an advanced Retrieval-Augmented Generation (RAG) chatbot that combines:

- A custom statistics knowledge base
- Semantic search using Sentence Transformers
- Vector retrieval using FAISS
- OpenAI GPT models for intelligent responses

Unlike traditional FAQ chatbots that return pre-written answers, this system retrieves relevant content from your own database and uses AI to generate context-aware explanations.

---

## Features

✅ Natural language question answering

✅ Retrieval-Augmented Generation (RAG)

✅ FAISS vector database

✅ OpenAI integration

✅ Statistics-focused educational assistant

✅ Fallback to GPT when no matching knowledge is found

✅ Easy deployment with Streamlit

---

## System Architecture

```text
User Question
      |
      v
Sentence Embedding
      |
      v
FAISS Vector Search
      |
      +---- Relevant Content Found
      |             |
      |             v
      |      OpenAI GPT
      |             |
      |             v
      |      Generated Answer
      |
      +---- No Relevant Content
                    |
                    v
              OpenAI GPT
                    |
                    v
              Generated Answer
```

---

## Project Structure

```text
statistics-ai-chatbot/

├── app.py
├── ingest.py
├── requirements.txt
├── .env
│
├── knowledge/
│   └── statistics_notes.csv
│
└── faiss_index/
    ├── statistics.index
    └── texts.pkl
```

---

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd statistics-ai-chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure OpenAI API Key

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Create Knowledge Base

Example CSV:

```csv
content
A p-value is the probability...
The Central Limit Theorem states...
Standard deviation measures variability...
Confidence intervals provide a range...
```

Save as:

```text
knowledge/statistics_notes.csv
```

---

## Build the Vector Database

```bash
python ingest.py
```

This creates:

```text
faiss_index/statistics.index
faiss_index/texts.pkl
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Example Questions

- What is a p-value?
- Explain the Central Limit Theorem.
- What is the difference between Type I and Type II errors?
- What is standard deviation?
- Explain confidence intervals.

---

## Future Improvements

- Multi-document PDF ingestion
- Research paper retrieval
- Citation support
- Conversation memory
- Hybrid search (keyword + vector)
- Voice assistant integration
- Fine-tuned statistics model

---

## Technologies Used

| Component | Technology |
|------------|------------|
| LLM | OpenAI GPT |
| Embeddings | Sentence Transformers |
| Vector Database | FAISS |
| Frontend | Streamlit |
| Language | Python |
| Data Storage | CSV / Documents |

---

## Author

Pasindu Sanjaya Dissanayake

BSc (Hons) Statistics & Operations Research

University of Peradeniya
