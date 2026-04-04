import subprocess


def retrieve(query, collection, k=4):
    """Retrieve top-k relevant chunks from ChromaDB."""
    results = collection.query(
        query_texts=[query],
        n_results=k
    )
    return results["documents"][0]


def generate_answer(question, retrieved_chunks, model="mistral"):
    """Generate answer using Ollama (local LLM)."""

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are an AI assistant answering questions about the Swiggy Annual Report.

STRICT RULES:
- Use ONLY the provided context
- If the answer is not present, say:
  "I could not find this in the Swiggy Annual Report."

Context:
{context}

Question:
{question}

Answer:
"""

    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        capture_output=True,
        text=True
    )

    return result.stdout.strip()
