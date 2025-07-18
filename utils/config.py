# utils/config.py
from dotenv import load_dotenv
import os

load_dotenv()

# Strip to prevent newline/space issues
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "").strip()

# ✅ Key masking for optional display
def _mask(key, visible=4):
    if not key or len(key) <= visible * 2:
        return '*' * len(key)
    return key[:visible] + '*' * (len(key) - visible * 2) + key[-visible:]

# ✅ DEBUG: Show loaded key status at startup
def debug_show_keys():
    print("🔐 OPENAI_API_KEY:", _mask(OPENAI_API_KEY))
    print("🔐 GITHUB_TOKEN:", _mask(GITHUB_TOKEN))

# ✅ Optional check utility
def is_openai_key_valid() -> bool:
    return bool(OPENAI_API_KEY) and len(OPENAI_API_KEY) > 20
