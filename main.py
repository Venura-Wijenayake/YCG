from modules.generator import generate_content
from modules.script_generator import save_output_to_file
from utils.key_validator import run_all_checks

# 🔥 New: Available content styles
CONTENT_STYLES = [
    "default",
    "top_5_list",
    "educational",
    "shorts",
    "product_review",
    "comedic"
]

def main():
    print("🎬 YouTube Content Generator")
    print("============================\n")

    # 🛑 Run key validation before anything else
    if not run_all_checks():
        print("\n🚫 Aborting due to invalid API keys.")
        return

    # 🧠 Main prompt loop
    while True:
        print("\nWhat would you like to do?")
        print("1️⃣  Generate new content")
        print("0️⃣  Quit")

        choice = input("\nEnter choice (1 or 0): ").strip()

        if choice == "0":
            print("👋 Exiting. See you next time!")
            return

        elif choice == "1":
            # 🔍 Prompt for format style first
            print("\n🎨 Choose a content format:")
            for i, style in enumerate(CONTENT_STYLES, 1):
                print(f"{i}. {style}")

            style_choice = input("\nEnter format number (1–6): ").strip()

            try:
                style_index = int(style_choice) - 1
                format_type = CONTENT_STYLES[style_index]
            except (ValueError, IndexError):
                print("⚠️ Invalid selection. Using 'default' format.")
                format_type = "default"

            topic = input("\nEnter a YouTube topic: ").strip()
            if not topic:
                print("⚠️ No topic entered. Returning to main menu.")
                continue

            print("\n⏳ Generating content, please wait...\n")
            result = generate_content(topic, format_type)  # 🔥 Pass format_type

            if result and all(result.values()):
                print("✅ Content generated successfully!\n")
                print("📌 Title:\n" + result['title'])
                print("\n📝 Description:\n" + result['description'])
                print("\n🏷️ Tags:\n" + result['tags'])
                print("\n🎤 Script:\n" + result['script'])

                save_output_to_file(
                    topic=topic,
                    title=result['title'],
                    tags=result['tags'],
                    script=result['script'],
                    description=result['description']
                )
            else:
                print("❌ Failed to generate content. Please check your API key and try again.")
        else:
            print("❗ Invalid choice. Please enter 1 or 0.")

if __name__ == "__main__":
    main()
