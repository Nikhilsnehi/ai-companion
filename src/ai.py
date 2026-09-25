from openai import OpenAI
import base64

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

previous_response_id = None


def ask_ai(question):
    global previous_response_id

    response = client.responses.create(
        model="llama3.2:3b",
        instructions="""
        You are an AI companion called Companion.

        Be conversational, natural, and helpful.
        Keep responses relatively concise unless the user asks for detail.
        Match the user's casual tone when appropriate.
        Do not sound overly formal or robotic.
        """,
        input=question,
        previous_response_id=previous_response_id
    )

    previous_response_id = response.id

    return response.output_text


def ask_about_screen(question):
    global previous_response_id

    with open("screen.png", "rb") as image_file:
        image_data = base64.b64encode(
            image_file.read()
        ).decode("utf-8")

    response = client.responses.create(
        model="llama3.2:3b",
        instructions="""
        You are an AI companion watching the user's screen.
        Describe what is actually visible in the image.
        Do not invent details that cannot be seen.
        Keep your response conversational and concise.
        """,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": question
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/png;base64,{image_data}"
                    }
                ]
            }
        ],
        previous_response_id=previous_response_id
    )

    previous_response_id = response.id

    return response.output_text