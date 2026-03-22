import chromadb

client = chromadb.Client()

def store_memory(workflow, result):

    collection = client.get_or_create_collection("workflow_memory")

    collection.add(
        documents=[workflow],
        ids=[str(hash(workflow))]
    )
