def parse_plot_points(phrases) -> dict:
    """
    Parses each phrase into a tone directive (before colon) and quote (after colon),
    if a colon exists. If no colon, it's treated as a quote only.

    Returns:
    {
        "tone_directives": [...],   # for influencing style
        "literal_quotes": [...]     # for strict inclusion in script
    }
    """
    tone_directives = []
    literal_quotes = []

    if not isinstance(phrases, list):
        print("⚠️ Warning: Expected a list of phrases, got:", type(phrases))
        return {
            "tone_directives": [],
            "literal_quotes": []
        }

    for phrase in phrases:
        if not isinstance(phrase, str):
            print(f"⚠️ Skipping invalid phrase (not a string): {phrase}")
            continue

        parts = phrase.split(":", 1)
        if len(parts) == 2:
            directive, quote = parts[0].strip(), parts[1].strip()
            if directive:
                tone_directives.append(directive)
            if quote:
                literal_quotes.append(quote)
        else:
            quote = phrase.strip()
            if quote:
                literal_quotes.append(quote)

    return {
        "tone_directives": tone_directives,
        "literal_quotes": literal_quotes
    }
