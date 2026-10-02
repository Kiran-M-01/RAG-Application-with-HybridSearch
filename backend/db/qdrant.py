from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid

client = QdrantClient(host="localhost", port=6333)

COLLECTION_NAME = "documents"

def create_collection(vector_size: int):
    collections = client.get_collections().collections
    exists = any(
        collection.name == COLLECTION_NAME 
        for collection in collections
    )

    if exists:      # IF THE COLLECTION ALREADY EXISTS, IT CAUSES AN ERROR WHEN TRYING TO CREATE IT AGAIN, SO WE JUST RETURN
        return

    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=vector_size,
            distance=Distance.COSINE
        )
    )

def store_embeddings(embeddings):
    points = []

    for item in embeddings:
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=item['embedding'],
                payload={"text": item['text']}
            )
    )
        
    client.upsert(collection_name=COLLECTION_NAME,points=points)