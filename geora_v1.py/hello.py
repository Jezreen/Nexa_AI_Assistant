import webbrowser
import pyttsx3
import datetime

def speak(text):
    print("Geora:", text)

    local_engine = pyttsx3.init()
    local_engine.say(text)
    local_engine.runAndWait()

while True:
    user = input("You: ").lower().strip()

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
        speak("Opening Chat GPT")
        webbrowser.open("https://chatgpt.com")

    elif "calculator" in user:
        speak("Opening Calculator")

    elif "who am i" in user:
        speak("You are Jezreen, creator of Geora.")

    elif "bye" in user:
        speak("Goodbye!")
        break

    else:
        speak("I don't understand.")