import os
from rag.pdf_to_text import pdf_to_text
from rag.chunking import chunk_text
from rag.embed_store import build_and_save_index, load_collection
from rag.rag_answer import retrieve, generate_answer

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")

PDF_PATH = os.path.join(DATA_DIR, "swiggy_report.pdf")


def ingest():
    """Process PDF and build ChromaDB index."""
    print("📄 Reading PDF...")
    text = pdf_to_text(PDF_PATH)

    print("✂️ Chunking text...")
    chunks = chunk_text(text)

    print(f"🔢 Total chunks: {len(chunks)}")

    print("🧠 Creating embeddings & ChromaDB index...")
    build_and_save_index(chunks)

    print("✅ Ingestion complete!")


def chat():
    """CLI chat loop."""

    # 🔥 Load vector DB
    collection = load_collection()

    print("\n🤖 Swiggy Annual Report QA Bot")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("You: ")

        if query.lower() in ["exit", "quit"]:
            break

        retrieved = retrieve(query, collection)

        answer = generate_answer(query, retrieved)

        print("\n📌 Answer:")
        print(answer)

        print("\n📚 Supporting Context:")
        for i, chunk in enumerate(retrieved, 1):
            print(f"\n--- Context {i} ---\n{chunk[:300]}...")


if __name__ == "__main__":
    print("1️⃣ Ingest PDF")
    print("2️⃣ Chat with bot")

    choice = input("Choose option: ")

    if choice == "1":
        ingest()
    elif choice == "2":
        chat()
    else:
        print("Invalid choice")
