import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("And the current date is ")
    speak(date)
    speak(month)
    speak(year)

def wishMe():
    speak("Welcome back, Sir")
    
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")

    speak("Zen at your service. Please tell me how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again, please...")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            print(query)
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif "offline" in query:
            quit()