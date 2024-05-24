from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

connection_uri = os.getenv('MONGO_URI')

client = MongoClient(connection_uri)

db = client.get_database("spark_chat")

chats_collection = db.get_collection("chat_rooms")

try:
    print("Connection established successfully using PyMongo!")
except Exception as e:
    print("Error connecting to MongoDB database:", e)

