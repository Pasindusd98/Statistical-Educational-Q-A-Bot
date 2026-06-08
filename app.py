import os
import faiss
import pickle
import numpy as np
import streamlit as st

from openai import OpenAI
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

index = faiss.read_index(
    "faiss_index/statistics.index"
)

with open(
    "faiss_index/texts.pkl",
    "rb"
) as f:
    documents = pickle.load(f)

SIMILARITY_THRESHOLD = 1.0

def retrieve_context(question):

    embedding = model.encode(
        [question]
    )

    distances, indices = index.search(
        np.array(embedding),
        k=3
    )

    results = []

    for d, idx in zip(
        distances[0],
        indices[0]
    ):
        if d < SIMILARITY_THRESHOLD:
            results.append(
                documents[idx]
            )

    return results

def chatbot(question):

    contexts = retrieve_context(
        question
    )

    if contexts:

        context_text = "\n\n".join(
            contexts
        )

        prompt = f"""
You are a statistics tutor.

Use the provided context.

Context:
{context_text}

Question:
{question}
"""

    else:

        prompt = f"""
You are a statistics tutor.

Answer the question using your
own knowledge.

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"system",
                "content":"You are an expert statistics educator."
            },
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content

st.title(
    "📊 Advanced Statistics AI Chatbot"
)

question = st.text_input(
    "Ask anything about statistics"
)

if question:

    answer = chatbot(
        question
    )

    st.write(answer)
