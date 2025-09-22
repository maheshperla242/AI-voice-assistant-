import speech_recognition as sr
import pyttsx3           # offline Text-To-Speech
import webbrowser
import sys
import wikipedia

# ---------- TTS Setup ----------
engine = pyttsx3.init()
def speak(text):
    print("January said:", text)
    engine.say(text)
    engine.runAndWait()

# ---------- Speech Recognition ----------
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language="en-in")
            print("You said:", command)
            return command.lower()
        except:
            speak("Sorry, I could not understand.")
            return ""

# ---------- Commands ----------
def myCommand(c):
    if "model" in c or "moodle" in c:
        webbrowser.open("https://cet.iitp.ac.in")

    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open github" in c:
        webbrowser.open("https://github.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif "google" in c or "search" in c:
        speak("What should I search?")
        topic = listen()
        if topic:
            webbrowser.open(f"https://www.google.com/search?q={topic}")
            speak(f"Here is what I found for {topic}")

    elif "information" in c or "tell me about" in c or "who is" in c:
        speak("What do you want to know?")
        topic = listen()
        if topic:
            try:
                info = wikipedia.summary(topic, sentences=2)
                speak(info)
            except:
                speak("Sorry, I couldn't find anything on that.")

    elif "good bye" in c or "exit" in c or "quit" in c:
        speak("Good bye boss, January going offline.")
        sys.exit(0)

# ---------- Main Loop ----------
if __name__ == "__main__":
    speak("Activating January...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            word = recognizer.recognize_google(audio)

            if word.lower() == "january":
                speak("Yes Boss")
                while True:
                    command = listen()
                    if command:
                        myCommand(command)

        except Exception as e:
            print("Error:", e)
