import chromadb

client = chromadb.Client()

def get_memory():
    return client.get_or_create_collection("workflow_memory")
