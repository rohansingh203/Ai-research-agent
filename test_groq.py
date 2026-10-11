
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Find the folder containing this Python file
BASE_DIR = Path(__file__).resolve().parent

# Load the API key from that folder's .env file
load_dotenv(BASE_DIR / ".env", override=True)

# Connect to Groq
client = Groq()

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Explain in two simple sentences why investors should check both the positive and negative sides of a company."
        }
    ],
    max_completion_tokens=300,
)

print(response.choices[0].message.content)