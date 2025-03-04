


from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel  # Assuming GeminiModel exists in pydantic_ai
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker
from alchemy import User, engine, Article
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams
from google import genai
from google.genai import types

# Initialize the session for SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()



# Gemini model setup in pydantic_ai
gemini_model_name = "text-embedding-004"  



# Initialize the Gemini model with the API key and model name


gemini_client = genai.Client(api_key="AIzaSyBjQGi3xxiGGSiKphfGa57XmGzYu2-syK8")
# Initialize the Qdrant client
client = QdrantClient(url="http://localhost:6333")

try:
    # Fetch collections to check if the connection works
    collections = client.get_collections()
    print("Collections:", collections)
except Exception as e:
    print(f"Connection failed: {e}")
#client.delete_collection(collection_name="articles")
# client.create_collection(
#     collection_name="articles",
#     vectors_config=VectorParams(
#         size=768,  # The size of the vectors you're using
#         distance="Cosine"  # Choose between 'Cosine', 'Euclidean', or 'Dot'
#     )
# )


# DocumentEmbedding Model using Pydantic
class DocumentEmbedding(BaseModel):
    title: str
    content: str
    embedding: list[float]  # Ensure embedding is a list of floats

    @classmethod
    def generate_embedding(cls, content: str):
        # Use Gemini through pydantic_ai for generating embeddings
        response = gemini_client.models.embed_content(
            model="text-embedding-004",
            contents=[content])
        # Ensure response.embeddings is a list and extract the first embedding
        if response.embeddings:
            embedding = response.embeddings[0].values  # Get the first embedding's values
        else:
            raise ValueError("No embeddings were returned by Gemini.")
    
        return embedding

    @classmethod
    def create_with_embedding(cls, title: str, content: str):
        # Generate embedding and return the instance
        embedding = cls.generate_embedding(content)
        return cls(title=title, content=content, embedding=embedding)


def add_article_to_vector_db(title: str, content: str):
    # Create the DocumentEmbedding instance with the generated embedding
    doc = DocumentEmbedding.create_with_embedding(title, content)
    
    # Upsert the document into Qdrant collection
    client.upsert(
        collection_name="articles",
        points=[PointStruct(id=len(content), vector=doc.embedding, payload={"title": title})]
    )
    print(f"Article added: {title} (vector DB)")


# Add existing articles to vector database
for article in session.query(Article).all():
    add_article_to_vector_db(article.title, article.content)    


def search_best_article(query: str):

    print("Embedding oluşturuluyor...")  # Kontrol için
    test_embedding = DocumentEmbedding.generate_embedding(query)
    print("Oluşturulan embedding:", test_embedding)  # Çıktıyı görmek için
    # Generate embedding for the query using the same model
    query_embedding = DocumentEmbedding.create_with_embedding(title="", content=query).embedding
    # Perform the search in the Qdrant collection
 
    search_results = client.search(
        collection_name="articles",
        query_vector=query_embedding,
        limit=1
    )
    
    if search_results:
        return search_results[0].payload["title"]
    return "Couldn't find any article!"    

def get_best_match(query: str):
    return search_best_article(query)
# # Test query
# query_text = "what is AI?"
# best_article = search_best_article(query_text)
# print(f"Best matching article: {best_article}")