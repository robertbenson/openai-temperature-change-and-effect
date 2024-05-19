from openai import OpenAI
from dotenv import load_dotenv
import os

client = OpenAI()

load_dotenv()
my_api_key = os.getenv("OPENAI_API_KEY")


def run_chat_for_temperature(temperature_req: float):
    print(f"\n\nRunning chat completion with a temperature of: {temperature}")
    completion = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=50,
        temperature=temperature_req,
        messages=[
            {"role": "system",
             "content": "You are a poetic assistant, skilled in explaining "
                        "complex programming concepts with creative flair."},
            {"role": "user",
             "content": "Compose a poem that explains the concept of "
                        "recursion in programming."}
        ]
    )
    print(completion.choices[0].message.content)


if __name__ == '__main__':
    for temperature in [0, 0.5, 1, 1.5, 2]:
        run_chat_for_temperature(temperature)
