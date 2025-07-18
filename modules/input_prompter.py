import difflib

VALID_FORMATS = [
    "default",
    "top_5_list",
    "educational",
    "shorts",
    "product_review",
    "comedic"
]

def get_fuzzy_formats(user_input: str) -> list:
    raw_inputs = [chunk.strip().lower().replace(" ", "_") for chunk in user_input.split("+")]
    results = []
    for entry in raw_inputs:
        match = difflib.get_close_matches(entry, VALID_FORMATS, n=1, cutoff=0.6)
        if match:
            results.append(match[0])
        else:
            print(f"⚠️ Unknown format: '{entry}' — skipping.")
    return results


def pre_prompt_flow(content_styles):
    """
    Collects all pre-generation inputs from the user.
    Returns a dictionary of user preferences.
    """
    print("\n🧠 Pre-Prompt Setup")
    print("====================\n")

    # 🎨 Flexible format selection
    print("💡 Enter your desired format(s) (e.g., 'shorts + top five'):")
    format_input = input("Enter format: ").strip()

    formats = get_fuzzy_formats(format_input)
    if not formats:
        print("⚠️ No valid formats detected. Defaulting to 'default'.")
        formats = ["default"]

    print(f"\n🎯 Using format: {' + '.join(formats)}")
    confirm = input("Are you sure? (y/n): ").strip().lower()
    if confirm != "y":
        print("❌ Format rejected. Returning to main menu.")
        return None

    # 🧠 Topic input
    topic = input("\nEnter a YouTube topic: ").strip()
    if not topic:
        print("⚠️ No topic entered. Returning to main menu.")
        return None

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
    must_use_phrases = []
    print("\nEnter up to 5 phrases or plot points that must appear in the script:")
    for i in range(5):
        phrase = input(f"Phrase {i+1} (or press Enter to skip): ").strip()
        if not phrase:
            break
        must_use_phrases.append(phrase)

    return {
        "style": formats,  # NOTE: this is now a list, not a single string
        "topic": topic,
        "manual_tags": manual_tags,
        "strict_tag_limit": strict_tag_limit,
        "custom_description": custom_description,
        "must_use_phrases": must_use_phrases
    }
