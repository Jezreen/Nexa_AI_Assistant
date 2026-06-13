import keyboard
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr

def speak(text):
    print("Geora:", text)

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(source, timeout=10)
            text = r.recognize_google(audio)

            print("You:", text)
            return text.lower()

        except:
            return ""

print("Geora is sleeping...")
print("Press F8 to activate")

keyboard.wait("f8")

speak("Geora Activated")

while True:

    user = listen()

    if user == "":
        speak("I did not hear anything")
        continue

    if "hi" in user or "hello" in user:
        speak("Hello Jezreen!")

    elif "open youtube" in user:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "time" in user:
        now = datetime.datetime.now().strftime("%H:%M")
        speak("Current time is " + now)

    elif "google" in user:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "date" in user:
        today = datetime.datetime.now().strftime("%d-%m-%Y")
        speak("Today's date is " + today)

    elif "chatgpt" in user:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")

    elif "google classroom" in user:
        speak("Opening Google Classroom")
        webbrowser.open("https://classroom.google.com")

    elif "who am i" in user:
        speak("You are Jezreen, creator of Geora.")

    elif "bye" in user:
        speak("Goodbye Jezreen")
        break

    else:
        speak("I don't understand")