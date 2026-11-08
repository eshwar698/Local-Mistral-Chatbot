# Local Mistral Chatbot

A local conversational chatbot experiment built with **Mistral 7B**, **Ollama**, and Python. The project also includes scripts for generating sample conversations, converting them into JSONL, and optionally uploading a dataset to Together AI.

## Overview

This project explores running a locally hosted language model with a custom assistant personality and building a small conversational dataset pipeline.

### Features

- Run Mistral 7B locally through Ollama.
- Send prompts through Ollama's chat API.
- Generate and save chatbot conversations as TXT files.
- Convert conversation TXT files into JSONL records.
- Configure an assistant personality using an Ollama `Modelfile`.
- Optionally upload a prepared dataset to Together AI.

## Architecture

```text
User Prompt / Random Question
          |
          v
Python Chatbot Script
          |
          v
Ollama Local API
          |
          v
Mistral 7B
          |
          v
Generated Response
          |
          v
Conversation TXT Files
          |
          v
TXT-to-JSONL Converter
          |
          v
data1.jsonl
          |
          v
Optional Together AI Upload
```

## Project Structure

```text
Local-Mistral-Chatbot/
├── mistral_script.py
├── txttojsonl.py
├── check.py
├── Modelfile
├── requirements.txt
└── .gitignore
```

Generated conversations and datasets are intentionally excluded from version control.

## Requirements

- Python 3.10 or later
- [Ollama](https://ollama.com/)
- Mistral model downloaded through Ollama
- Together AI account/API key (optional, for dataset upload)

## Setup

### 1. Install Ollama and Mistral

Install Ollama and download the model:

```bash
ollama pull mistral
```

Start Ollama before running the chatbot.

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate conversations

Run:

```bash
python mistral_script.py
```

The script sends prompts to the local Ollama API and saves generated conversations as TXT files.

The script currently uses a Windows data directory (`D:\data`). Update the `data_folder` variable if you want to use another location.

### 4. Convert conversations to JSONL

Place generated TXT files inside a `data/` directory in the project folder.

Run:

```bash
python txttojsonl.py
```

The converter produces `data1.jsonl` containing conversation records formatted with `<|user|>` and `<|bot|>` markers.

### 5. Optional: Upload dataset to Together AI

Set your API key as an environment variable.

PowerShell:

```powershell
$env:TOGETHER_API_KEY="your-api-key"
```

Then ensure `data1.jsonl` exists in the project directory and run:

```bash
python check.py
```

Never commit API keys or `.env` files.

## Assistant Personality

The Ollama `Modelfile` defines a sarcastic, chaotic, humorous assistant personality. Its temperature setting is configured to encourage varied responses.

## Limitations

- This is an experimental project, not a production chatbot.
- Conversations are generated locally and are not included in this repository.
- The current chatbot script sends each prompt as a separate request rather than maintaining conversational history.
- Dataset conversion uses a simple text format and is not a general-purpose conversation parser.
- Dataset upload does not itself fine-tune a model.
- Model behavior depends on the installed Ollama model and local hardware.

## Technologies

- Python
- Mistral 7B
- Ollama
- Requests
- JSONL
- Together AI Python SDK

## Author

**Eshwar Lankalapalli**

GitHub: [eshwar698](https://github.com/eshwar698)
