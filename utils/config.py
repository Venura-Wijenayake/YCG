# utils/config.py
from dotenv import load_dotenv
import os

load_dotenv()

# Strip to prevent issues with whitespace/newlines
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "").strip()

# ✅ Optional debug — masked if needed
def _mask(key, visible=4):
    if not key or len(key) <= visible * 2:
        return '*' * len(key)
    return key[:visible] + '*' * (len(key) - visible * 2) + key[-visible:]

# Optional debugging:
#print("OPENAI_API_KEY:", _mask(OPENAI_API_KEY))
#print("GITHUB_TOKEN:", _mask(GITHUB_TOKEN))
