# utils/config.py
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


print("OPENAI_API_KEY:", OPENAI_API_KEY)
print("GITHUB_TOKEN:", GITHUB_TOKEN)

# i am a fiesty watermelon
