def pre_prompt_flow(_) -> dict:
    """
    Collects all pre-generation inputs from the user.
    Returns a dictionary of user preferences.
    """

    print("\n🧠 Pre-Prompt Setup")
    print("====================\n")

    # 🧠 Topic first
    topic = input("Enter a YouTube topic: ").strip()
    if not topic:
        print("⚠️ No topic entered. Returning to main menu.")
        return None

    # 🎨 Style input
    print("\n💡 Describe the desired tone, pacing, and structure (e.g., 'funny, fast-paced, top five style'):")
    style_description = input("Style description: ").strip()

    # 🏷️ Manual tag input
    manual_tags = []
    tag_input = input("\nEnter up to 15 tags (comma-separated, or leave blank): ").strip()
    if tag_input:
        manual_tags = [t.strip() for t in tag_input.split(",") if t.strip()]
        if len(manual_tags) > 15:
            print("⚠️ Too many tags entered. Truncating to 15.")
            manual_tags = manual_tags[:15]

    # 🚫 Strict tag limit
    strict_input = input("\nStrictly enforce 15-tag limit? (y/n): ").strip().lower()
    strict_tag_limit = strict_input == "y"

    # 📝 Description override
    custom_description = ""
    desc_input = input("\nWould you like to enter a custom description? (y/n): ").strip().lower()
    if desc_input == "y":
        custom_description = input("Enter your custom description: ").strip()

    # 🧩 Must-use phrases or plot points
    raw_phrases = []
    print("\nEnter up to 5 phrases or plot points that must appear in the script:")
    for i in range(5):
        phrase = input(f"Phrase {i+1} (or press Enter to skip): ").strip()
        if not phrase:
            break
        raw_phrases.append(phrase)

    return {
        "topic": topic,
        "style": style_description,
        "manual_tags": manual_tags,
        "strict_tag_limit": strict_tag_limit,
        "custom_description": custom_description,
        "must_use_phrases": raw_phrases  # 🟢 Plain strings — now correct
    }
