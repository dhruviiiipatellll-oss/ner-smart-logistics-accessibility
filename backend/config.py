import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/ner_logistics")
    API_V1_STR = "/api/v1"
    PROJECT_NAME = "NER Smart Logistics Platform"
    MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN", "")
    MODEL_PATH = os.getenv("MODEL_PATH", "./ml-models/trained_models")
    NER_STATES = [
        "Assam", "Meghalaya", "Manipur", "Mizoram",
        "Nagaland", "Arunachal Pradesh", "Sikkim", "Tripura"
    ]

settings = Settings()