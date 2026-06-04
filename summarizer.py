import os
from openai import OpenAI

# Load API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes text clearly and simply."
            },
            {
                "role": "user",
                "content": f"Summarize this text:\n\n{text}"
            }
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("AI Text Summarizer (OpenAI)")
    print("---------------------------")

    text = input("Enter text to summarize:\n")

    summary = summarize_text(text)

    print("\nSummary:\n", summary)