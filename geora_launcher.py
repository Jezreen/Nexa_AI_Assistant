import keyboard
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

print("Geora is sleeping...")
print("Press F8 to activate")

keyboard.wait("f8")

print("Geora Activated!")

speak("Geora Activated")