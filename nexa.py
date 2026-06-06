import keyboard
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import os


def speak(text):
    print("Nexa:", text)

    local_engine = pyttsx3.init()
    local_engine.say(text)
    local_engine.runAndWait()

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        try:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=10)
            text = r.recognize_google(audio)

            print("You:", text)
            return text.lower()

        except:
            return None

print("Nexa is sleeping...")
print("Press F8 to activate")

keyboard.wait("f8")

speak("Nexa Activated")

speak("Testing voice")

WAKE_WORDS = ["jarvis", "alexa", "nexa"]

while True:

    user = listen()

    if user is None:
        continue

    if not any(word in user for word in WAKE_WORDS):
        continue

    print("WAKE WORD DETECTED")

    for word in WAKE_WORDS:
        user = user.replace(word, "")

    user = user.strip()

    print("COMMAND =", user)

    if user == "":
        speak("Yes Jezreen")
        continue

    print("COMMAND =", user)

    # Greetings
    if user == "hello" or user == "hi":
        speak("Hello Jezreen")

    # YouTube
    elif "youtube" in user:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Google
    elif "google" in user:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # WhatsApp
    elif "whatsapp" in user:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    # ChatGPT
    elif "chatgpt" in user or "chat gpt" in user:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")

    # Time
    elif "time" in user:
        now = datetime.datetime.now().strftime("%H:%M")
        speak("Current time is " + now)

    # Date
    elif "date" in user:
        today = datetime.datetime.now().strftime("%d-%m-%Y")
        speak("Today's date is " + today)

    elif "chrome" in user:
        speak("Opening Chrome")
        os.system("start chrome")

    elif "vscode" in user or "vs code" in user:
        speak("Opening VS Code")
        os.system("code")

    elif "explorer" in user or "file explorer" in user or "folder" in user:
        speak("Opening File Explorer")
        os.system("explorer")

    # Calculator
    elif "calculator" in user:
        speak("Opening Calculator")
        os.system("calc")

    # Notepad
    elif "notepad" in user:
        speak("Opening Notepad")
        os.system("notepad")

    # Recall Memory

    elif "what do you remember" in user:

        try:
            with open("memory.txt", "r") as f:
                memories = f.read()

            if memories:
                speak(memories)

            else:
                speak("I do not remember anything")

        except:
            speak("Memory file not found")

    
    # Remember

    elif "remember" in user:

        memory = user.replace("remember", "").strip()

        with open("memory.txt", "a") as f:
            f.write(memory + "\n")

        speak("I will remember that")


    # Clear Memory

    elif "forget everything" in user:

        open("memory.txt", "w").close()

        speak("All memories deleted")

    # Identity
    elif "who am i" in user:
        speak("You are Jezreen, creator of Nexa")

    # Exit
    elif "stop" in user or "bye" in user:
        speak("Goodbye Jezreen")
        break

    else:
        speak("Command not found")