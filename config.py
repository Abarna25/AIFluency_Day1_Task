from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

MODEL = os.getenv("MODEL")

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

QUESTIONS = [
    "What is Abarna's mark?",
    "Who scored highest?",
    "What is the average mark?",
    "Which students scored above 85?"
]