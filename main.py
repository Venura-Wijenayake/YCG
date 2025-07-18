from modules.generator import generate_content
from modules.script_generator import save_output_to_file
from modules.input_prompter import pre_prompt_flow
from modules.script_parser import parse_output_file
from utils.key_validator import run_all_checks
from utils.plot_point_parser import parse_plot_points  # ✅ Optional debug import

def main():
    print("🎬 YouTube Content Generator")
    print("============================\n")

    if not run_all_checks():
        print("\n🚫 Aborting due to invalid API keys.")
        return

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
            print("\n🟡 [Main] Collecting user input...")
            user_inputs = pre_prompt_flow([])
            if not user_inputs:
                print("❌ Input aborted or invalid.")
                continue

            # ✅ Debug output for parsed plot points
            parsed = parse_plot_points(user_inputs["must_use_phrases"])
            print("\n📊 Parsed Tone Directives:")
            if parsed["tone_directives"]:
                for td in parsed["tone_directives"]:
                    print(f" - {td}")
            else:
                print(" - (None)")

            print("📌 Literal Quotes:")
            if parsed["literal_quotes"]:
                for q in parsed["literal_quotes"]:
                    print(f" - \"{q}\"")
            else:
                print(" - (None)")

            print("\n🟡 [Main] Preparing to call generate_content()...")
            print(f"🔍 Topic: {user_inputs['topic']}")
            print(f"🔍 Style Desc: {user_inputs['style']}")
            print(f"🔍 Tags: {user_inputs['manual_tags']}")
            print(f"🔍 Strict tags: {user_inputs['strict_tag_limit']}")
            print(f"🔍 Must-use: {user_inputs['must_use_phrases']}")
            print(f"🔍 Custom Desc: {user_inputs['custom_description']}")

            print("\n⏳ Generating content, please wait...\n")
            result = generate_content(
                topic=user_inputs["topic"],
                style_description=user_inputs["style"],
                manual_tags=user_inputs["manual_tags"],
                strict_tag_limit=user_inputs["strict_tag_limit"],
                custom_description=user_inputs["custom_description"],
                must_use_phrases=user_inputs["must_use_phrases"]
            )

            if not result:
                print("🔴 Generation failed — empty result.")
                continue

            if not result.get("script"):
                print("⚠️ Script data missing — check section headers or prompt format.")
                continue

            print("✅ Content generated successfully!\n")
            print("📌 Title:\n" + result.get('title', ''))
            print("\n📝 Description:\n" + result.get('description', ''))
            print("\n🏷️ Tags:\n" + result.get('tags', ''))
            print("\n🎤 Script:\n" + result['script'])

            approve = input("\n🔒 Approve this script for voice/video generation? (y/n): ").strip().lower()
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

                print("\n🟡 Regenerating content...")
                result = generate_content(
                    topic=parsed["topic"],
                    style_description="default structure, helpful tone",
                    custom_description=parsed["description"],
                    must_use_phrases=[],  # ⚠ Legacy files don't store style hints
                    manual_tags=parsed["tags"].split(","),
                    strict_tag_limit=True
                )

                if not result:
                    print("🔴 Regeneration failed — empty result.")
                    continue

                if not result.get("script"):
                    print("⚠️ Regenerated script is missing.")
                    continue

                print("✅ Regenerated successfully!\n")
                print("📌 Title:\n" + result.get('title', ''))
                print("\n📝 Description:\n" + result.get('description', ''))
                print("\n🏷️ Tags:\n" + result.get('tags', ''))
                print("\n🎤 Script:\n" + result['script'])

                approve = input("\n🔒 Approve this regenerated script? (y/n): ").strip().lower()
                if approve != "y":
                    print("❌ Rejected. Returning to main menu.")
                    continue

                save_output_to_file(
                    topic=parsed['topic'],
                    title=result['title'],
                    tags=result['tags'],
                    script=result['script'],
                    description=result['description']
                )

            except Exception as e:
                print(f"❌ Failed to load or parse file: {e}")

        else:
            print("❗ Invalid choice. Please enter 1, 2, or 0.")

if __name__ == "__main__":
    main()
