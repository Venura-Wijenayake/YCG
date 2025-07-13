# script_generator.py

import os
from datetime import datetime

def save_output_to_file(topic: str, title: str, tags: str, script: str, description: str, output_dir: str = "outputs"):
    """
    Saves the generated YouTube script and metadata to a timestamped text file.
    """
    # Create a filename-safe version of the topic
    safe_topic = "".join(c if c.isalnum() or c in (' ', '-') else "_" for c in topic).strip().replace(" ", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{safe_topic}_{timestamp}.txt"

    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Topic\n{topic}\n\n")
        f.write(f"# Title\n{title}\n\n")
        f.write(f"# Description\n{description}\n\n")
        f.write(f"# Tags\n{tags}\n\n")
        f.write(f"# Script\n{script}\n")

    print(f"\n✅ Output saved to {filepath}")
