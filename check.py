import os
from together import Together

api_key = os.getenv("TOGETHER_API_KEY")

if not api_key:
    raise RuntimeError("Set the TOGETHER_API_KEY environment variable first.")

client = Together(api_key=api_key)

file_path = "data1.jsonl"

if not os.path.exists(file_path):
    raise FileNotFoundError(f"Dataset not found: {file_path}")

response = client.files.upload(
    file=file_path,
    purpose="fine-tune"
)

print("Upload successful.")
print("File ID:", response.id)
