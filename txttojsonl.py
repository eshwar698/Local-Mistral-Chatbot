import json
from pathlib import Path

DATA_DIR = Path("data")
OUTPUT_FILE = Path("data1.jsonl")

def convert_conversation(file_path):
    content = file_path.read_text(encoding="utf-8")
    user_marker = "USER:"
    bot_marker = "BOT:"

    if user_marker not in content or bot_marker not in content:
        return None

    user_text, bot_text = content.split(bot_marker, 1)
    user_text = user_text.split(user_marker, 1)[-1].strip()
    bot_text = bot_text.strip()

    if not user_text or not bot_text:
        return None

    return {
        "text": f"<|user|>\n{user_text}\n<|bot|>\n{bot_text}"
    }

def main():
    if not DATA_DIR.exists():
        raise FileNotFoundError(
            "Create a data/ folder containing conversation TXT files."
        )

    files = sorted(DATA_DIR.glob("*.txt"))
    converted = 0

    with OUTPUT_FILE.open("w", encoding="utf-8") as outfile:
        for file_path in files:
            conversation = convert_conversation(file_path)

            if conversation:
                outfile.write(json.dumps(conversation, ensure_ascii=False) + "\n")
                converted += 1

    print(f"Converted {converted}/{len(files)} conversations.")
    print(f"Dataset saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
