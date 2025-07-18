import os
import openai
from datetime import datetime
from utils.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def interpret_style_input(user_input: str, topic: str) -> str:
    """
    Given a natural language style description and topic,
    return a fully structured script-style prompt using OpenAI.
    Also logs input/output to logs/.
    """
    print("\n🟡 [Style GPT] Interpreting style input...")

    system_prompt = (
        "You are an expert YouTube script designer. Given a description of desired tone, structure, and pacing, "
        "you will create a GPT-friendly prompt to generate a YouTube video script. Your response should include "
        "the structure, mood, voice, and word count range. Use clear formatting."
    )

    user_prompt = f"""
User style input: "{user_input.strip()}"
Topic: "{topic.strip()}"

Now return a full prompt that tells GPT how to create a YouTube script with that style.
Only output the prompt. Do not explain anything else.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=600
        )

        prompt_output = response.choices[0].message["content"].strip()

        # 🔖 Ensure correct response format at end of prompt
        prompt_output += "\n\nRespond using this format:\n\n" \
                         "Title: ...\n" \
                         "Description: ...\n" \
                         "Tags: ...\n" \
                         "Script: ..."

        # 🧾 Log session
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_path = os.path.join(LOG_DIR, f"style_log_{timestamp}.txt")
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("=== OPENAI_API_KEY USED ===\n")
            f.write(OPENAI_API_KEY[:5] + "..." + OPENAI_API_KEY[-5:] + "\n\n")
            f.write("=== USER INPUT ===\n")
            f.write(user_input + "\n\n")
            f.write("=== TOPIC ===\n")
            f.write(topic + "\n\n")
            f.write("=== GPT PROMPT OUTPUT ===\n")
            f.write(prompt_output + "\n")

        print("🟢 [Style GPT] Style interpreted successfully.")
        print("✅ [Style GPT] Interpretation complete.")
        return prompt_output

    except Exception as e:
        print(f"🔴 [Style GPT] Error during style interpretation: {e}")
        return f"""Generate a YouTube script for the topic: "{topic}".

Respond using this format:

Title: ...
Description: ...
Tags: ...
Script: ...
"""
