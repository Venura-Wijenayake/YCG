from modules.generator import generate_content
from modules.script_generator import save_output_to_file
from modules.input_prompter import pre_prompt_flow
from modules.script_parser import parse_output_file  # 🆕 new import
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
        print("2️⃣  Regenerate from existing file")
        print("0️⃣  Quit")

        choice = input("\nEnter choice (1, 2, or 0): ").strip()

        if choice == "0":
            print("👋 Exiting. See you next time!")
            return

        elif choice == "1":
            # 🧠 Use new pre_prompt_flow
            user_inputs = pre_prompt_flow(CONTENT_STYLES)
            if not user_inputs:
                continue  # aborted or empty input

            print("\n⏳ Generating content, please wait...\n")
            result = generate_content(
                topic=user_inputs["topic"],
                format_type=user_inputs["style"],
                manual_tags=user_inputs["manual_tags"],
                strict_tag_limit=user_inputs["strict_tag_limit"],
                custom_description=user_inputs["custom_description"],
                must_use_phrases=user_inputs["must_use_phrases"]
            )

            if result and all(result.values()):
                print("✅ Content generated successfully!\n")
                print("📌 Title:\n" + result['title'])
                print("\n📝 Description:\n" + result['description'])
                print("\n🏷️ Tags:\n" + result['tags'])
                print("\n🎤 Script:\n" + result['script'])

                # 🔒 Approval Checkpoint
                approve = input("\n🔍 Approve this script for voice/video generation? (y/n): ").strip().lower()
                if approve != "y":
                    print("❌ Script rejected. Returning to main menu.")
                    continue

                save_output_to_file(
                    topic=user_inputs['topic'],
                    title=result['title'],
                    tags=result['tags'],
                    script=result['script'],
                    description=result['description']
                )
            else:
                print("❌ Failed to generate content. Please check your API key and try again.")

        elif choice == "2":
            filepath = input("\n📂 Enter path to the edited script file: ").strip()
            try:
                parsed = parse_output_file(filepath)
                print("\n✅ File loaded. Here's what was extracted:")
                for key, value in parsed.items():
                    print(f"- {key.capitalize()}: {value[:60]}{'...' if len(value) > 60 else ''}")

                confirm = input("\nUse this to regenerate? (y/n): ").strip().lower()
                if confirm != "y":
                    print("❌ Regeneration canceled.")
                    continue

                print("\n⏳ Regenerating based on your edits...\n")
                result = generate_content(
                    topic=parsed["topic"],
                    format_type="default",  # can enhance later to detect or ask
                    custom_description=parsed["description"],
                    must_use_phrases=[],  # future: detect key phrases from script
                    manual_tags=parsed["tags"].split(","),
                    strict_tag_limit=True
                )

                if result and all(result.values()):
                    print("✅ Regenerated successfully!\n")
                    print("📌 Title:\n" + result['title'])
                    print("\n📝 Description:\n" + result['description'])
                    print("\n🏷️ Tags:\n" + result['tags'])
                    print("\n🎤 Script:\n" + result['script'])

                    # 🔒 Approval Checkpoint
                    approve = input("\n🔍 Approve this script for voice/video generation? (y/n): ").strip().lower()
                    if approve != "y":
                        print("❌ Script rejected. Returning to main menu.")
                        continue

                    save_output_to_file(
                        topic=parsed['topic'],
                        title=result['title'],
                        tags=result['tags'],
                        script=result['script'],
                        description=result['description']
                    )
                else:
                    print("❌ Regeneration failed.")

            except Exception as e:
                print(f"❌ Failed to load or parse file: {e}")

        else:
            print("❗ Invalid choice. Please enter 1, 2, or 0.")

if __name__ == "__main__":
    main()
