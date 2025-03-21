from pymongo import MongoClient
from config import MONGODB_URI, DATABASE_NAME

def get_db():
    """
    Returns a MongoDB database object.
    """
    client = MongoClient(MONGODB_URI)
    return client[DATABASE_NAME]
