import openai
import os
from datetime import datetime

from utils.config import OPENAI_API_KEY
from utils.plot_point_parser import parse_plot_points  # ✅ Updated interface
from modules.style_enforcer import apply_signature_tone
from modules.style_interpreter import interpret_style_input

openai.api_key = OPENAI_API_KEY

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def generate_content(
    topic: str,
    style_description: str = "",
    manual_tags: list = None,
    strict_tag_limit: bool = False,
    custom_description: str = "",
    must_use_phrases: list = None
) -> dict:
    print("\n🟡 [Content GPT] Starting full script generation...")

    if manual_tags is None:
        manual_tags = []
    if must_use_phrases is None:
        must_use_phrases = []

    # ✅ Step 1: Parse plot points
    parsed = parse_plot_points(must_use_phrases)
    tone_directives = parsed["tone_directives"]
    literal_quotes = parsed["literal_quotes"]

    # ✅ Step 2: Merge tone guidance into style description
    combined_style = style_description.strip()
    if tone_directives:
        combined_style += "\n\nIncorporate tone ideas like: " + "; ".join(tone_directives)

    # ✅ Step 3: Build prompt
    prompt = interpret_style_input(combined_style, topic)
    prompt += apply_signature_tone()

    # ✅ Step 4: Add instructions
    extra_instructions = ""

    if literal_quotes:
        extra_instructions += "\n\nThese exact phrases must appear in the script: "
        extra_instructions += ", ".join(f'"{q}"' for q in literal_quotes)

    if custom_description:
        extra_instructions += f"\n\nUse this description instead of generating one: \"{custom_description}\""

    if manual_tags:
        tag_note = ", ".join(manual_tags)
        if strict_tag_limit:
            extra_instructions += f"\n\nOnly use these tags (max 15): {tag_note}"
        else:
            extra_instructions += f"\n\nStart with these tags and add more if helpful (max 15 total): {tag_note}"

    prompt += extra_instructions

    # ✅ Step 5: Call OpenAI
    try:
        print("\n🟡 [Content GPT] Sending final script generation prompt to OpenAI...")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for YouTube content creators."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800,
        )

        content = response.choices[0].message["content"]
        print("🟢 [Content GPT] Script content received from OpenAI!")

        # ✅ Log everything
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_path = os.path.join(LOG_DIR, f"content_log_{timestamp}.txt")
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("=== TOPIC ===\n")
            f.write(topic + "\n\n")
            f.write("=== PROMPT ===\n")
            f.write(prompt + "\n\n")
            f.write("=== RESPONSE ===\n")
            f.write(content.strip() + "\n")

        # ✅ Extract from response
        data = {"title": "", "description": "", "tags": "", "script": ""}
        current_section = None

        for line in content.splitlines():
            lower = line.strip().lower()
            if lower.startswith("title:"):
                current_section = "title"
                data[current_section] = line.split(":", 1)[1].strip()
            elif lower.startswith("description:"):
                current_section = "description"
                data[current_section] = line.split(":", 1)[1].strip()
            elif lower.startswith("tags:"):
                current_section = "tags"
                data[current_section] = line.split(":", 1)[1].strip()
            elif lower.startswith("script:"):
                current_section = "script"
                data[current_section] = ""
            elif current_section:
                data[current_section] += line.strip() + "\n"

        # Final cleanup
        for k in data:
            data[k] = data[k].strip()

        # ✅ Validation Warnings
        if not data["script"]:
            print("🔴 [Content GPT] ❗ Script content not found in parsed response!")
        if not data["title"]:
            print("🟡 [Content GPT] ⚠ Title not detected.")
        if not data["description"]:
            print("🟡 [Content GPT] ⚠ Description not detected.")
        if not data["tags"]:
            print("🟡 [Content GPT] ⚠ Tags not detected.")

        return data

    except Exception as e:
        print(f"🔴 [Content GPT] Error generating content: {e}")
        return {}
