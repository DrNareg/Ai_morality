import os
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from the .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "bababouy?",
        },
    ],
)
print(completion.choices[0].message.content)