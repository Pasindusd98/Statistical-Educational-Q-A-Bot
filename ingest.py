import pandas as pd
import faiss
import pickle

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

df = pd.read_csv(
    "knowledge/statistics_notes.csv"
)

texts = df["content"].tolist()

embeddings = model.encode(
    texts,
    convert_to_numpy=True
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(embeddings)

faiss.write_index(
    index,
    "faiss_index/statistics.index"
)

with open(
    "faiss_index/texts.pkl",
    "wb"
) as f:
    pickle.dump(texts, f)

print("Knowledge base created.")
