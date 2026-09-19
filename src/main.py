from dotenv import load_dotenv
from ai import shoot

load_dotenv()

print("we here")

while True:
    question = input("me: ")

    if question.lower() == "exit":
        print("im out peace")
        break

    answer = shoot(question)

    print("AI:", answer)