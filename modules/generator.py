# modules/generator.py

import openai
import os
from utils.config import OPENAI_API_KEY
from modules.template_manager import build_prompt
from modules.style_enforcer import apply_signature_tone  # ✅ Inject signature tone

openai.api_key = OPENAI_API_KEY  # Apply key globally

def generate_content(
    topic: str,
    format_type: str = "default",
    manual_tags: list = None,
    strict_tag_limit: bool = False,
    custom_description: str = "",
    must_use_phrases: list = None
) -> dict:
    """
    Generates a full YouTube content package based on the topic and selected format style.
    Accepts manual inputs to influence the result.
    """
    if manual_tags is None:
        manual_tags = []
    if must_use_phrases is None:
        must_use_phrases = []

    # 🧩 Compose additional instructions
    extra_instructions = ""

    if must_use_phrases:
        extra_instructions += "\n\nIncorporate the following phrases or plot points into the script: "
        extra_instructions += ", ".join(f'"{p}"' for p in must_use_phrases)

    if custom_description:
        extra_instructions += f"\n\nUse this description instead of generating one: \"{custom_description}\""

    if manual_tags:
        tag_note = ", ".join(manual_tags)
        if strict_tag_limit:
            extra_instructions += f"\n\nOnly use these tags (max 15): {tag_note}"
        else:
            extra_instructions += f"\n\nStart with these tags and add more if helpful (max 15 total): {tag_note}"

    # 🧠 Build prompt with structure + tone + instructions
    base_prompt = build_prompt(topic, format_type)
    style_tone = apply_signature_tone()
    prompt = base_prompt + style_tone + extra_instructions

    try:
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

        # 📦 Parse GPT output
        lines = content.splitlines()
        data = {"title": "", "description": "", "tags": "", "script": ""}
        key = None

        for line in lines:
            if line.lower().startswith("title:"):
                key = "title"
                data[key] = line.split(":", 1)[1].strip()
            elif line.lower().startswith("description:"):
                key = "description"
                data[key] = line.split(":", 1)[1].strip()
            elif line.lower().startswith("tags:"):
                key = "tags"
                data[key] = line.split(":", 1)[1].strip()
            elif line.lower().startswith("script:"):
                key = "script"
                data[key] = ""
            elif key:
                data[key] += line.strip() + "\n"

        return data

    except Exception as e:
        print("❌ Error generating content:", e)
        return {}
