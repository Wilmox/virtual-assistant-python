import os
import openai
import speech_recognition
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY", default=None)

OPENAI_COMPLETION = openai.Completion()
MAX_TOKENS = 10

# response = openai.Model.retrieve("text-davinci-002")

def answer_question(question):
  prompt = f"You: {question}\n J.A.R.V.I.S.: "
  response = OPENAI_COMPLETION.create(
    model="text-davinci-002",
    prompt=prompt,
    temperature=0.5,
    max_tokens=MAX_TOKENS,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["You"]
  )
  return response.choices[0].text.strip()


if __name__ == '__main__':
  print(answer_question(input("Question: ")))