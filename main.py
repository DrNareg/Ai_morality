import os
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from the .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_openai_completion(prompt):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return completion.choices[0].message.content

# Example usage
prompts = ["write hi","write bye"]

for prompt in prompts:
    # Get response
    ai_response = get_openai_completion(prompt)
    # Print the AI's response
    print(ai_response)
