# Problem Statement : Document Similarity
## find the document that is most similar to the input query from user using hugging face embedding model, downloaded locally and using cosine similarity





# Import HuggingFaceEmbeddings.
# It loads a pre-trained embedding model from Hugging Face
# and provides methods to convert text into numerical vectors.
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity


# Load the embedding model.
#
# model_name:
# Specifies which pre-trained embedding model to use.
#
# "sentence-transformers/all-MiniLM-L6-v2"
# is a lightweight model that converts text into
# 384-dimensional vector embeddings.
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# List of input documents.
# Each document is a string that will be converted
# into its corresponding vector representation.
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about bumrah"


# Convert all documents into embeddings.
#
# embed_documents():
# - Accepts a list of text documents.
# - Generates one embedding vector for each document.
# - Returns a list of vectors.
doc_embeddings = embedding.embed_documents(documents)

query_embedding = embedding.embed_query(query)

# Calculate the similarity between the query embedding
# and each document embedding.
#
# cosine_similarity():
# Returns a similarity score between -1 and 1.
# A higher score indicates greater semantic similarity.
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Find the document with the highest similarity score.
#
# enumerate(scores):
# Pairs each score with its document index.
#
# sorted(...):
# Sorts the (index, score) pairs based on similarity score.
#
# [-1]:
# Selects the pair with the highest score.
index, score = sorted(
    list(enumerate(scores)),
    key=lambda x: x[1]
)[-1]


# Print the user's query.
print(query)

# Print the document that best matches the query.
print(documents[index])

# Print the similarity score.
print("Similarity Score:", score)