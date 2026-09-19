from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

print("we movin bby")

while True:
    question = input("me: ")

    if question.lower() == "exit":
        print("we out peace")
        break

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=question
    )

    print("AI:", response.output_text)