import os
#  Disable all telemetry + warnings 
os.environ["ANONYMIZED_TELEMETRY"] = "false"
os.environ["CHROMA_TELEMETRY"] = "false"
os.environ["CHROMA_DISABLE_TELEMETRY"] = "1"
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["PYTHONWARNINGS"] = "ignore"


from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama


def main():

    print("\nLoading data...")

    # 1. Load text
    loader = TextLoader("ambedkar.txt")
    documents = loader.load()

    # 2. Split text into chunks
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    # 3. Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. Create vector DB
    vectordb = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory="db"
    )
    vectordb.persist()

    # 5. Create proper retriever (using new API — invoke)
    retriever = vectordb.as_retriever()

    # 6. LLM (small model to avoid RAM error)
    llm = Ollama(model="llama3.2:1b")   # Make sure you pulled it

    print("\nReady! Ask questions about Ambedkar.\n")

    while True:
        query = input("Ask: ").strip()
        if query.lower() in ["exit", "quit"]:
            print("\nGoodbye!")
            break

        # ---- Retrieve relevant text chunks (no deprecation warning) ----
        results = retriever.invoke(query)

        context = "\n".join([doc.page_content for doc in results])

        # Prompt to LLM
        prompt = (
            "Use the context below to answer the question.\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {query}\nAnswer:"
        )

        # ---- Safe LLM call ----
        try:
            answer = llm.invoke(prompt)
            print("\nAnswer:", answer, "\n")
        except Exception as e:
            print("\nLLM Error:", e, "\n")


if __name__ == "__main__":
    main()












