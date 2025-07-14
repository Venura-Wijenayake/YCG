# utils/key_validator.py

import os
import openai
import requests

def check_openai_key():
    key = os.getenv("OPENAI_API_KEY", "")
    if not key:
        return False
    try:
        openai.api_key = key
        openai.Model.list()
        return True
    except Exception:
        return False

def check_github_token():
    token = os.getenv("GITHUB_TOKEN", "")
    if not token:
        return False
    try:
        headers = {"Authorization": f"token {token}"}
        r = requests.get("https://api.github.com/user", headers=headers, timeout=5)
        return r.status_code == 200
    except Exception:
        return False

def run_all_checks():
    print("🔑 Validating your keys...\n")
    openai_valid = check_openai_key()
    github_valid = check_github_token()

    print("🧠 OpenAI:", "✅ Valid" if openai_valid else "❌ Invalid")
    print("🐙 GitHub:", "✅ Valid" if github_valid else "❌ Invalid")

    return openai_valid and github_valid
