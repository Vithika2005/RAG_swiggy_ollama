import chromadb

DB_DIR = "chroma_db"


def build_and_save_index(chunks):
    """Create ChromaDB collection with persistent storage."""

    chroma_client = chromadb.PersistentClient(path=DB_DIR)

    collection = chroma_client.get_or_create_collection(
        name="swiggy_report"
    )

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks
    )

    print("✅ ChromaDB index created and persisted.")


def load_collection():
    chroma_client = chromadb.PersistentClient(path=DB_DIR)
    return chroma_client.get_collection(name="swiggy_report")
