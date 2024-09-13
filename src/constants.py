from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-K1N4XBkXXJuMNX_V9ee0XM5uj9l-G4N1OZW7N-oN_iT3BlbkFJO-4kHPMH2DkvXWATsKrT-GVD5igRv91JeQ2NzdPisA")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "gpt-4-0125-preview")
USER = os.getenv("USER", "root")
PASSWORD = os.getenv("PASSWORD", "MamaGrentina$100!")
HOST = os.getenv("HOST", "127.0.0.1")
DATABASE = os.getenv("DATABASE", "ecommerce")
PORT = int(os.getenv("PORT", 3306))
