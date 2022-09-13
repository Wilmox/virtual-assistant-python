import os
import openai
import speech_recognition
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY", default=None)

OPENAI_COMPLETION = openai.Completion()
MAX_TOKENS = 20

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

def listener():
  recognizer = speech_recognition.Recognizer()
  with speech_recognition.Microphone() as speech:
    print("👂 Listening...")
    recognizer.pause_threshold = 2
    audio = recognizer.listen(speech)
    
    try:
      print("🔍 Recognizing your ✨Beautiful✨ voice...")
      query = recognizer.recognize_google(audio, language="en-US")
      print(f'You said: "{query}" ')
            
    except Exception as e:
      print("❌ I didn't quite get that...")
      return "I didn't quite get that"
    return query
    

if __name__ == '__main__':
  query = listener()
  answer = answer_question(query)
  print(answer)