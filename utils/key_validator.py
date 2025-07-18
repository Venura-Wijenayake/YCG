import os
import openai
import requests

def check_openai_key():
    key = os.environ.get("OPENAI_API_KEY", "")
    if not key:
        print("❌ OpenAI key not found in environment.")
        return False
    try:
        openai.api_key = key
        openai.Model.list()
        return True
    except Exception as e:
        print(f"❌ OpenAI key invalid or failed to connect: {e}")
        return False

def check_github_token():
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        print("❌ GitHub token not found in environment.")
        return False
    try:
        headers = {"Authorization": f"token {token}"}
        response = requests.get("https://api.github.com/user", headers=headers, timeout=5)
        if response.status_code == 200:
            return True
        else:
            print(f"❌ GitHub token rejected: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ GitHub token check failed: {e}")
        return False

def run_all_checks():
    print("🔑 Validating your keys...\n")
    openai_valid = check_openai_key()
    github_valid = check_github_token()

    print("🧠 OpenAI:", "✅ Valid" if openai_valid else "❌ Invalid")
    print("🐙 GitHub:", "✅ Valid" if github_valid else "❌ Invalid")

    return openai_valid and github_valid
