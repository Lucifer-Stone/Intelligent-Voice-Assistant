import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 - David, 1 - Zira

def speak(audio):
    engine.say(audio) # speaks the argument audio
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am Jarvis, you're friendly voice assistant at your service.")
    speak("Please tell me how can I help you?")
    
def takeCommand():
    #It takes microphone input from the user and returns string output
    
    r = sr.Recognizer() # helps in audio recognition
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
        
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences = 2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strfttime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'open code' in query:
            codePath_c = r"C:\Users\Salman\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath_c)

        elif 'open brave' in query:
            codePath_b = "C:\Program Files\BraveSoftware\Brave-Browser\Application"
            os.startfile(codePath_b)
        
        elif 'quit' in query:
            exit()