import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(com):
    if "open youtube" in com.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open google" in com.lower():
        webbrowser.open("https://www.google.com")
    elif "open linkedin" in com.lower():
        webbrowser.open("https://www.linkedin.com/feed")
    elif "open github" in com.lower():
        webbrowser.open("https://github.com")

if __name__ == "__main__":
    speak("Hey Boss! I am Jarvis")
while True:
    root = sr.Recognizer()
    print("Recognizing...")
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = root.listen(source, timeout=2, phrase_time_limit=1)
            command = root.recognize_google(audio)
        if(command.lower() == "jarvis"):
            speak("yes")
            with sr.Microphone() as source:
             print("Jarvis Activated...")
             audio = root.listen(source)
             command = root.recognize_google(audio)
             processcommand(command)

    except Exception as e:
         print("Error; {0}".format(e))

        

