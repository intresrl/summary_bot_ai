import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def summary_with_gpt3(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Riassumi questo testo estratto da un messaggio audio che ho ricevuto. Inoltre proponimi una risposta veloce che potrei dare a chi mi ha inviato il messaggio"
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0,
        max_tokens=1024
    )

    return response.choices[0].message.content
