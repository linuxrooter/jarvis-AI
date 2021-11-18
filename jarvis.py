import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia #pip install wikipedia
import pyaudio #pip install PyAudio


from pyttsx3.engine import Engine

engine = pyttsx3.init()
engine.say("Hello boss")
engine.runAndWait()          


engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voices', voice[0].id)
newVoiceRate =120
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("This is JARVIS")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

date()

def wishme():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good morning")
    elif hour >= 12 and hour <= 17:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good evening")    
    else:
        speak("Good night")
    speak("JARVIS at your service. How can i Help you?")

     
wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing......")
        query = r.recognize_google(audio,'en=US')
        print("query")
    except Exception as e:
        print(e)
        speak("say that again please..")

        return "None"

    return query


takeCommand()

if __name__== "__main__":
    wishme()

    while True:
        query = takeCommand.lower()
        print(query)


        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching.....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentence = 2)
            speak(result)

    



 

