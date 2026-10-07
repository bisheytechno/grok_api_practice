import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(question, system="You are a helpful assistant."):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",    # ← Free!
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": question}
        ]
    )
    return response.choices[0].message.content


print(ask_ai("What is Python in one line?"))
print("---")

print(ask_ai(
    "What is OOP?",
    system="You are a Python expert. Answer in 2 lines only."
))
print("---")

print(ask_ai("What is machine learning?"))