# utils/config.py
from dotenv import load_dotenv
import os

load_dotenv()

# Strip to prevent issues with whitespace/newlines
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "").strip()

print("OPENAI_API_KEY:", OPENAI_API_KEY)
print("GITHUB_TOKEN:", GITHUB_TOKEN)

# i am a feisty watermelon boy
