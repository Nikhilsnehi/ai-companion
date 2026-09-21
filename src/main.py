from dotenv import load_dotenv
from ai import ask_ai, ask_about_screen
from screen import capture_screen

print("AI Companion is running.")

while True:
    question = input("me: ")

    if question.lower() == "exit":
        print("AI Companion shutting down.")
        break

    if question.lower() == "look":
        capture_screen()
        answer = ask_about_screen("What am I looking at?")
    else:
        answer = ask_ai(question)

    print("AI:", answer)