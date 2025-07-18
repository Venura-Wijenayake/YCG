def apply_signature_tone(tone_override: str = None) -> str:
    """
    Returns a prompt fragment that guides GPT to mimic a signature YouTube storytelling tone.
    Optionally override with a custom tone block (e.g., 'chaotic monologue').
    """
    if tone_override:
        return f"\n\nStyle Guide:\n{tone_override.strip()}\n"

    return """
Style Guide:
- Voice: Gravitas-laden, serious but grounded. Reflect the weight of galactic events without melodrama.
- Tone: Cinematic, confident, with a thread of poetic mystery or implied tragedy.
- Perspective: Third-person narrator (omniscient, but emotionally tuned)
- Sentences: Vary pace — mix punchy one-liners with longer, flowing descriptions.
- Don’t invent anything. Use only what's verifiably in the provided content.
- Never summarize casually — build drama. Every line should feel like a reveal.
- Use proper nouns and canon-specific terms as often as possible.
- Avoid filler phrases like "let me explain" or "you may be wondering".
- Hook early with mystery or tension.
- End on emotional or thematic resonance (not summary).
"""
