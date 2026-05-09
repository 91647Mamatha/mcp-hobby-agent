import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def extract_from_context(text):
    prompt = f"""
You are given profile data of a person from multiple sources.

Your job is to extract hobbies and interests ONLY.

Rules:
- Remove all duplicates
- Combine similar hobbies into one
- Return as a clean numbered list
- No explanations, no headings, no extra text
- Ignore education, work, skills, achievements

Text:
{text}
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def ask_directly(name):
    prompt = f"""
List hobbies or personal interests of {name}.
Return only hobbies, one per line.
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content