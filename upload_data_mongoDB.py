import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load environment variables
load_dotenv()

# Get credentials from .env
username = quote_plus(os.getenv("MONGO_USER"))
password = quote_plus(os.getenv("MONGO_PASSWORD"))

# Build MongoDB URI with database specified
mongo_uri = f"mongodb+srv://{username}:{password}@cluster0.jrmb9uy.mongodb.net/spamhamDb?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(mongo_uri)

# Load CSV
csv_file_path = r"C:\Users\sharm\Downloads\spam_detection\notebooks\spamham.csv"
df = pd.read_csv(csv_file_path)

# Access DB and collection
db = client["spamhamDb"]
collection = db["Message"]

# Upload data
spam_copy = df.to_dict(orient="records")
collection.insert_many(spam_copy)

print(f"Inserted {len(spam_copy)} documents into MongoDB collection!")
