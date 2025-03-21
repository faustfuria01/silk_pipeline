import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
QUALYS_API_URL = os.getenv("QUALYS_API_URL")
CROWDSTRIKE_API_URL = os.getenv("CROWDSTRIKE_API_URL")
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
