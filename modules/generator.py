import openai
import os
from utils.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY  # This automatically applies bearer auth

def generate_content(topic: str) -> dict:
    prompt = f"""Generate a full YouTube content package based on the topic: "{topic}".
    
1. Title (engaging, <60 chars)
2. Description (SEO-friendly, 2–3 sentences)
3. Tags (10–15, comma-separated)
4. Script (full video narration, 200–300 words)

Respond in the following format:
Title: ...
Description: ...
Tags: ...
Script:
...
"""

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

        # Parsing stays the same
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
