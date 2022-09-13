import os
import sys
import openai
import speech_recognition
import pyttsx3
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY", default=None)

OPENAI_COMPLETION = openai.Completion()
MAX_TOKENS = 100

# 0 is a male voice
# 1 is a female voice
VOICE = 1 

# ENGINE SYMTHESIZERS
# sapi5 = Windows XP, Vista, 8, 8.1, 10, 11
# espeak = Ubuntu Desktop 8.10, 9.04, 9.10
engine=pyttsx3.init('sapi5')
engine.setProperty('volume', 0.5)
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[VOICE].id)

def answer_question(question):
  try:
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
  except Exception as e:
    print(e)
    sys.exit()

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
  
def speak(sentence):
  try:
    engine.say(sentence)
    engine.runAndWait()
  except Exception as e:
    print(e)
    

if __name__ == '__main__':
  query = listener()
  answer = answer_question(query)
  print('Response: \n \t \t' + answer + '\n')
  speak(answer)