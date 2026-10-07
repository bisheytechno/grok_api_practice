# Groq API Practice

Learning how to call AI APIs using Groq — free and fast LLM API for AI engineering projects.

---

## What This Covers

- Groq client setup with API key
- System prompts — controlling AI behavior
- Asking questions and getting responses
- .env for secure API key storage
- Reusable ask_ai() function

---

## Tech Stack

- Python 3.x
- Groq SDK
- python-dotenv
- openai/gpt-oss-20b model

---

## Project Structure

```
grok_api_practice/
│
├── myvenv/
├── .env              → API key 
├── .gitignore        → .env hidden
├── grok_api.py       → Main code
└── README.md
```

---

## How to Run

**1. Clone:**
```bash
git clone https://github.com/bisheytechno/grok_api_practice.git
cd grok_api_practice
```

**2. Virtual Environment:**
```bash
python -m venv myvenv
myvenv\Scripts\activate
```

**3. Install:**
```bash
pip install groq python-dotenv
```

**4. Add API Key:**
```
# .env file 
GROQ_API_KEY=gsk_your_key_here
```

**5. Run:**
```bash
python grok_api.py
```

---

## Example Output

```
Python is a high-level, interpreted programming language
known for its readable syntax and rapid development.
---
OOP organizes code around objects that encapsulate data
and behavior, promoting reusability through inheritance.
---
Machine learning is a branch of AI where computers learn
from data rather than being explicitly programmed...
```

---

## Key Concepts

| Concept | What it does |
|---------|-------------|
| system role | Controls AI personality and behavior |
| user role | Your question to the AI |
| ask_ai() | Reusable function for any question |

---


## Author

**Bishal KC** — Aspiring AI Engineer

---

## License

MIT License