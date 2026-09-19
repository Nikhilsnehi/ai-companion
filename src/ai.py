from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

previous_response_id = None


def shoot(question):
    global previous_response_id

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=question,
        previous_response_id=previous_response_id
    )

    previous_response_id = response.id

    return response.output_text