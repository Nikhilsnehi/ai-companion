from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def shoot(question):
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=question
    )

    return response.output_text
