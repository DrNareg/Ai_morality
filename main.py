import os
from dotenv import load_dotenv
from openai import OpenAI
from tabulate import tabulate

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

def format_text(text, max_line_length=40):
    # Insert line breaks to format the text
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:
            current_line += f"{word} "
        else:
            lines.append(current_line.strip())
            current_line = f"{word} "

    lines.append(current_line.strip())
    return "\n".join(lines)

# Example usage
prompts = ["write hi", "write I am here my friend from overseas"]

# Create a list to store rows of the table
table_data = []

for prompt in prompts:
    # Template will be used to make prompts list shorter
    template = "what is 10+10?"
    full_prompt = prompt + ", " + template

    # Get response
    ai_response = get_openai_completion(full_prompt)

    # Format the prompt and response with line breaks
    formatted_prompt = format_text(full_prompt)
    formatted_response = format_text(ai_response)

    # Append formatted prompt and response as a tuple to the table_data list
    table_data.append((formatted_prompt, formatted_response))

# Specify the file path
file_path = "output_responses.txt"

# Open the file in write mode
with open(file_path, 'w') as file:
    # Write the formatted table to the file
    file.write(tabulate(table_data, headers=["Prompt", "Response"], tablefmt="grid", colalign=("left", "left")))

print(f"Responses have been written to {file_path}")
