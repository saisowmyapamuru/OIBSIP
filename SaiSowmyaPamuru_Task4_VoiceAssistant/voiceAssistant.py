import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        return command.lower()

    except:
        return ""

speak("Hello, I am your voice assistant.")

while True:

    command = listen()

    if "hello" in command:
        speak("Hello Sai Sowmya")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")

    elif "date" in command:
        today = datetime.date.today()
        speak(f"Today's date is {today}")

    elif "stop" in command:
        speak("Goodbye")
        break