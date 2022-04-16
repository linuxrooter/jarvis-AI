
import pyttsx3 #pip install pyttsx3
import datetime
from rsa import PrivateKey, PublicKey
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib
import rsa
from subprocess import call

engine = pyttsx3.init('sapi5')
engine.say("Hello boss")
engine.runAndWait()

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voices', voice[1].id)
newVoiceRate = 210
engine.setProperty('rate', newVoiceRate)

class CallPy(object):
    def __init__(self, path='C:\Users\ps946\Desktop\python\namp.py'):
        self.path = path

    def __call__python_file(self):
        call(["Python3", "{}".format(self.path)])

if __name__=="__main__":
    c =CallPy()
    c.__call__python_file()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("This is Friday")

def time():
    Time = datetime.datetime.now().strftime('current time is %H:%M:%S')
    speak(Time)

time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)

date()

def wishme():
    speak("Welcome back sir")
    hour = datetime.datetime.now().hour

    if hour >= 6  and hour <= 12:
        speak("Good morning")
    if hour >=12 and hour <= 16.59:
        speak("Good Afternoon")
    if hour >= 17 and hour <= 24:
        speak("Good Evening")
    if hour >= 24.1 and hour <= 6:
        speak("Good night")
    speak("Friday in your service. How can I help you")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def encryptor():
    PublicKey, PrivateKey = rsa.newkeys(512)
    file =input("Enter file location and name")
    print(file)
    encFile =rsa.enrypt(file.encode(),PublicKey)
    print("encrypted file", encFile)

def decryptor():
    input("Enter the encrypted filr location and name")
    decFile = rsa.decrypt(decFile, PrivateKey).decode()




def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= "en-US")
        print(query)
    except Exception as e:
        print(e)
        speak("say that again, please...")

        return "None"

    return query

if __name__ == "__main__":

    wishme()

    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'offline' in query:
            quit()

        elif 'what is your name' in query:
            result = 'my name is friday'
            speak(result)

        elif 'who are you' in query:
            result = "I am Friday version 1 point O your personal assistant. I am programmed to minor tasks like opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather In different cities, get top headline news from times of india and you can ask me computational or geographical questions too! "
            speak(result)
               
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'log out' in query:
            os.system("shutdown -1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1") 

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Pankaj sharma")
            print("I was built by Pankaj sharma")

        elif'what can you do' in query:
            result = "I can control your system"
            speak(result)
            

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)

        elif ' song name' in query:
             webbrowser.open("www.youtube.com/song name")

            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'search in chrome' in query:
            speak("what should i search")
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome %s'
            search = takeCommand().lower()
            webbrowser.get(chromepath).open_new_tab(search +" .com ")


        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Boss. I am not able to send this email")

        elif 'can you sing a song' in query:
            speak( "yes i can but you have to tell me song name")
            search = takeCommand().lower()
            webbrowser.open('youtube.com' + search)

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'encrypt' in query:
            file = takeCommand().lower()
            print("file")
            encryptor().file()


takeCommand()
    




