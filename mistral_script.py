import os
import datetime
import random
import requests

# ANSI color codes
YELLOW = "\033[93m"
NEON_GREEN = "\033[92m"
RESET_COLOR = "\033[0m"

# System message for the AI
chatbot1 = "You are a AI chatbot. Use harsh and strong language "

# Use Ollama's local Mistral model
def mistral7b(user_input):
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "mistral",
            "messages": [
                {"role": "system", "content": chatbot1},
                {"role": "user", "content": user_input}
            ],
            "stream": False
        }
    )

    result = response.json()
    return result.get("message", {}).get("content", "[No response]")

# List of random questions
questions = [
    "Hello, can you teach me to code Rust?",
    "Hey, could you explain why 2+2=5? in simple terms",
    "Hello!",
    "Hey, I'm feeling kinda lost in my career, any advice?",
    "yo, what is up dog?",
    "Hello! would you recommend using AI?",
    "Hey, any plans for the weekend?",
    "Hey, can you give me a helping hand?",
    "Hey, how can I improve my public speaking skills?",
    "Hello, can you suggest a good book for personal development?",
    "Hey, you look fat",
    "Why does my cat suddenly sprint around the house at 3 AM?",
    "Can you explain how quantum entanglement works in simple terms?",
    "What's the difference between jealousy and envy?",
    "How do I build a strong morning routine?",
    "Why do I keep procrastinating even when I know it's bad?",
    "What's a quick recipe I can make with just eggs, bread, and cheese?",
    "Is it bad to drink coffee right before bed?",
    "How do I know if someone is truly my friend or just being polite?",
    "What's the best way to memorize a long speech?",
    "Can you help me come up with a funny caption for this photo?",
    "Why do I always feel more productive at night?",
    "How can I get over the fear of public speaking?",
    "Whatâ€™s the correct way to use a semicolon?",
    "Why do we get dÃ©jÃ  vu?",
    "Is it better to study for long hours or take breaks in between?",
    "What are some underrated movies I should watch?",
    "Can you summarize this article in a few sentences?",
    "Why do my knees crack when I squat?",
    "Whatâ€™s the best strategy to win at rock-paper-scissors?"
]

# Create folder in D:\data
data_folder = r"D:\data"
os.makedirs(data_folder, exist_ok=True)

# Loop 400 times
for i in range(400):
    question = random.choice(questions)
    print(YELLOW + f"\nQuestion {i+1}: {question}" + RESET_COLOR)
    response = mistral7b(question)
    print(NEON_GREEN + response + RESET_COLOR)

    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"Response_{i+1}_{timestamp}.txt"
    file_path = os.path.join(data_folder, filename)

    content = f"USER: {question}\nBOT: {response}"

    with open(file_path, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

    print(f"Saved response to {file_path}")
