import time
from ai import ask_ai, ask_about_screen
from screen import capture_screen


print("AI Companion is running.")

screen_words = ["look", "screen", "watching", "see", "happening"]

while True:
    question = input("me: ")

    if question.lower() == "exit":
        print("AI Companion shutting down.")
        break

    if any(word in question.lower() for word in screen_words):
        print("Switch to the window you want me to see...")
        time.sleep(3)
        capture_screen()
        answer = ask_about_screen(question)
    else:
        answer = ask_ai(question)
    print("AI:", answer)