# main.py

from modules.generator import generate_content
from modules.script_generator import save_output_to_file  # Adjust if needed

def main():
    print("🎬 YouTube Content Generator")
    print("============================\n")

    topic = input("Enter a YouTube topic: ").strip()
    if not topic:
        print("⚠️ No topic entered. Exiting.")
        return

    print("\n⏳ Generating content, please wait...\n")
    result = generate_content(topic)

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

if __name__ == "__main__":
    main()
