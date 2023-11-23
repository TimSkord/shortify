import os
from dotenv import load_dotenv

load_dotenv()
DB_ENDPOINT = os.environ.get("DB_ENDPOINT", "")
DB_USERNAME = os.environ.get("DB_USERNAME", "")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME", "")

REQUEST_DB_CONNECTION_STRING = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_ENDPOINT}/{DB_NAME}"
