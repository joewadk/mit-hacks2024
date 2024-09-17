from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')
# This was a test of openai's embeddings. disreagard this file


embeddings_model = OpenAIEmbeddings(api_key=OPEN_AI_KEY)

embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)
print(len(embeddings))