# utils/key_reset.py

import os

# ✅ Allow only these keys to be reset
VALID_KEYS = {"OPENAI_API_KEY", "GITHUB_TOKEN"}

def update_key(env_key_name: str, new_value: str):
    lines = []
    updated = False

    if os.path.exists(".env"):
        with open(".env", "r") as f:
            for line in f:
                if line.startswith(env_key_name + "="):
                    lines.append(f"{env_key_name}={new_value}\n")
                    updated = True
                else:
                    lines.append(line)

    if not updated:
        lines.append(f"{env_key_name}={new_value}\n")

    with open(".env", "w") as f:
        f.writelines(lines)

    print(f"✅ {env_key_name} updated in .env")

def interactive_reset():
    print("🔐 Reset a key in your .env file")
    key = input("Which key? (e.g., OPENAI_API_KEY / GITHUB_TOKEN): ").strip()

    # ✅ Validate against known keys
    if key not in VALID_KEYS:
        print(f"❌ Invalid key. Allowed keys: {', '.join(VALID_KEYS)}")
        return

    new_value = input(f"Enter new value for {key}: ").strip()
    update_key(key, new_value)

if __name__ == "__main__":
    interactive_reset()
