# modules/template_manager.py

"""
template_manager.py

Handles YouTube script prompt templates for different video types and structures.
Keeps prompt logic out of generator.py and supports future format expansions.
"""

from typing import Literal

# Define supported content styles for prompting
SupportedFormat = Literal[
    "default",
    "top_5_list",
    "educational",
    "shorts",
    "product_review",
    "comedic"
]

def build_prompt(topic: str, format_type: SupportedFormat = "default") -> str:
    """
    Generate a GPT-friendly prompt for a given topic and format type.

    Args:
        topic (str): The YouTube topic input by the user.
        format_type (str): The desired content format.

    Returns:
        str: A formatted prompt string for OpenAI's API.
    """

    if format_type == "default":
        return f"""Generate a full YouTube content package based on the topic: "{topic}".

1. Title: Engaging and clear (max 60 characters)
2. Description: Short (2–3 sentences), informative, SEO-friendly
3. Tags: 10–15 comma-separated YouTube tags
4. Script: Full narration (200–300 words), informal and helpful

Respond in the following format:

Title: ...
Description: ...
Tags: ...
Script: ...
"""

    elif format_type == "top_5_list":
        return f"""Create a YouTube video script in a "Top 5 List" format based on the topic: "{topic}".

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
"""

    elif format_type == "educational":
        return f"""Generate an educational YouTube script for the topic: "{topic}".

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
"""

    elif format_type == "shorts":
        return f"""Create a short YouTube script (under 60 seconds) for the topic: "{topic}".

1. Title: Eye-catching (max 40 characters)
2. Description: 1–2 sentence hook
3. Tags: 10 short-form video tags
4. Script: Punchy, fast-paced, ideally 100–150 words

Respond in this format:

Title: ...
Description: ...
Tags: ...
Script: ...
"""

    elif format_type == "product_review":
        return f"""Generate a YouTube product review script for: "{topic}"

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
"""

    elif format_type == "comedic":
        return f"""Write a funny YouTube video script for the topic: "{topic}"

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

    else:
        raise ValueError(f"❌ Unsupported format type: '{format_type}'")
