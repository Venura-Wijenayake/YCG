"""
template_manager.py

Handles YouTube script prompt templates for different video types and structures.
Keeps prompt logic out of generator.py and supports future format expansions.
"""

from typing import Optional, List

# Canonical templates
TEMPLATE_MAP = {
    "default": """Generate a full YouTube content package based on the topic: "{topic}".{extras}

1. Title: Engaging and clear (max 60 characters)
2. Description: Short (2–3 sentences), informative, SEO-friendly
3. Tags: 10–15 comma-separated YouTube tags
4. Script: Full narration (200–300 words), informal and helpful

Respond in the following format:

Title: ...
Description: ...
Tags: ...
Script: ...
""",

    "top_5_list": """Create a YouTube video script in a "Top 5 List" format based on the topic: "{topic}".{extras}

1. Title: Attention-grabbing (max 60 characters)
2. Description: Brief (2–3 sentences), SEO-focused
3. Tags: 10 relevant tags
4. Script: Include an intro, then 5 numbered list items with 1–2 sentences each. Conclude with an outro.

Respond in this format:

Title: ...
Description: ...
Tags: ...
Script:
Intro: ...
1. ...
2. ...
3. ...
4. ...
5. ...
Outro: ...
""",

    "educational": """Generate an educational YouTube script for the topic: "{topic}".{extras}

1. Title: Clear and informative (max 60 characters)
2. Description: 2–3 sentences, suitable for students or general audiences
3. Tags: 10 educational tags
4. Script: Break into sections like Introduction, Explanation, Real-World Example, Summary

Respond in this format:

Title: ...
Description: ...
Tags: ...
Script:
Introduction: ...
Explanation: ...
Example: ...
Summary: ...
""",

    "shorts": """Create a short YouTube script (under 60 seconds) for the topic: "{topic}".{extras}

1. Title: Eye-catching (max 40 characters)
2. Description: 1–2 sentence hook
3. Tags: 10 short-form video tags
4. Script: Punchy, fast-paced, ideally 100–150 words

Respond in this format:

Title: ...
Description: ...
Tags: ...
Script: ...
""",

    "product_review": """Generate a YouTube product review script for: "{topic}"{extras}

1. Title: Honest and eye-catching (max 60 characters)
2. Description: 2–3 sentence review summary
3. Tags: 10 product-related tags
4. Script: Include pros, cons, personal opinion, and recommendation

Respond like this:

Title: ...
Description: ...
Tags: ...
Script:
Intro: ...
Pros: ...
Cons: ...
Verdict: ...
""",

    "comedic": """Write a funny YouTube video script for the topic: "{topic}"{extras}

1. Title: Witty or pun-based (max 60 characters)
2. Description: 2–3 sentence teaser with humor
3. Tags: Comedy tags
4. Script: Must include jokes, exaggeration, punchlines

Respond like this:

Title: ...
Description: ...
Tags: ...
Script:
Intro: ...
Bit 1: ...
Bit 2: ...
Outro: ...
"""
}


def build_prompt(
    topic: str,
    format_type: List[str],  # ⚠️ expects list of styles now
    manual_tags: Optional[list] = None,
    strict_tag_limit: bool = False,
    custom_description: str = "",
    must_use_phrases: Optional[list] = None
) -> str:
    """
    Generate a GPT-friendly prompt using the first matched format in the list.
    """
    if manual_tags is None:
        manual_tags = []
    if must_use_phrases is None:
        must_use_phrases = []

    # Supplementary instructions
    extra_lines = []

    if must_use_phrases:
        joined = ", ".join(f'"{p}"' for p in must_use_phrases)
        extra_lines.append(f"Incorporate the following phrases or plot points into the script: {joined}")

    if custom_description:
        extra_lines.append(f"Use this exact description instead of generating one: \"{custom_description}\"")

    if manual_tags:
        tag_line = ", ".join(manual_tags)
        if strict_tag_limit:
            extra_lines.append(f"Only use these tags (max 15): {tag_line}")
        else:
            extra_lines.append(f"Start with these tags and add more if needed (max 15 total): {tag_line}")

    extras = "\n\n" + "\n".join(extra_lines) if extra_lines else ""

    # Use first valid format from the list
    for fmt in format_type:
        if fmt in TEMPLATE_MAP:
            return TEMPLATE_MAP[fmt].format(topic=topic, extras=extras)

    # Fallback if no formats matched
    print("⚠️ No valid prompt format found. Defaulting to 'default'.")
    return TEMPLATE_MAP["default"].format(topic=topic, extras=extras)
