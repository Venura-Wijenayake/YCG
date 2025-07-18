import os

def parse_output_file(filepath: str) -> dict:
    """
    Parses a saved .txt output file and returns a dictionary
    with topic, title, description, tags, and script.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    fields = {"topic": "", "title": "", "description": "", "tags": "", "script": ""}
    current_key = None

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith("# Topic"):
                current_key = "topic"
                continue
            elif line.startswith("# Title"):
                current_key = "title"
                continue
            elif line.startswith("# Description"):
                current_key = "description"
                continue
            elif line.startswith("# Tags"):
                current_key = "tags"
                continue
            elif line.startswith("# Script"):
                current_key = "script"
                continue

            if current_key:
                if fields[current_key]:
                    fields[current_key] += "\n" + line
                else:
                    fields[current_key] = line

    return fields
