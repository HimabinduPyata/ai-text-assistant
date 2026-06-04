# AI Text Assistant (Summarizer Tool)

A simple Python-based AI tool that summarizes long text using OpenAI’s GPT model.

This project demonstrates how to integrate LLM APIs into a real-world application using clean code and environment variables.

---

## ✨ Features
- Summarizes long paragraphs into short, clear text
- Uses OpenAI GPT-4o mini model
- Command-line interface (CLI)
- Secure API key handling using environment variables

---

## 🧠 Example

### Input:
AI is transforming the world. It is used in healthcare, education, and finance...

### Output:
AI is transforming industries like healthcare, education, and finance by improving efficiency and automation.

---

## 🛠️ Tech Stack
- Python
- OpenAI API
- Git & GitHub

---

## ⚙️ Setup Instructions

### 1. Install dependencies
```bash
pip install openai

### 2. Set environment variable
export OPENAI_API_KEY="your_api_key_here"

### 3. Run the project
python3 summarizer.py