import smtplib
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import wikipedia

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint) 

engine = pyttsx3.init('sapi5')
engine.runAndWait()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) 
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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


class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text
        return text

    def JARVIS(self):
        wishme()
        while True:
            self.query = self.STT()

            if "hello" in self.query:
                speak("Hello, how can I help you?")
            elif "what's your name" in self.query:
                speak("I am Jarvis, your AI assistant.")
        

            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'offline' in self.query:
                sys.exit()

            elif 'what is your name' in self.query:
                result = 'my name is friday'
                speak(result)
        


            elif 'who are you' in self.query:
                result = "I am Friday version 1 point O your personal assistant. I am programmed to minor tasks like opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather In different cities, get top headline news from times of india and you can ask me computational or geographical questions too! "
                speak(result)
                
            elif 'open google' in self.query:
                webbrowser.open("google.com")
                
            elif 'log out' in self.query:
                os.system("shutdown -1")

            elif 'shutdown' in self.query:
                os.system("shutdown /s /t 1")

            elif 'restart' in self.query:
                os.system("shutdown /r /t 1") 

            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")
                
            elif "who made you" in self.query or "who created you" in self.query or "who discovered you" in self.query:
                speak("I was built by Pankaj sharma")
                print("I was built by Pankaj sharma")

            elif'what can you do' in self.query:
                result = "I can control your system"
                speak(result)
                

            elif 'search' in self.query:
                self.query = self.query.replace("search", "")
                webbrowser.open_new_tab(self.query)
                time.sleep(5)

            elif ' song name' in self.query:
                webbrowser.open("www.youtube.com/song name")

                
            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")


            elif 'email' in self.query:
                try:
                    speak("What should I say?")
                    content =self.STT()
                    to = "harryyourEmail@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Boss. I am not able to send this email")

            elif 'can you sing a song' in self.query:
                speak( "yes i can but you have to tell me song name")
                search =self.STT()
                webbrowser.open('youtube.com' + search)


            elif 'news' in self.query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                time.sleep(6)


                


FROM_MAIN, _ = loadUiType(os.path.join(os.path.dirname(__file__), "D:/AI/Real AI/scifi.ui"))

class Main(QMainWindow, FROM_MAIN):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.exitB.setStyleSheet("background-image:D:/AI/Real AI/lib/exit.png;/n"
                                "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)

        self.listenButton = QPushButton('Listen', self)
        self.listenButton.setGeometry(100, 500, 100, 30)
        self.listenButton.clicked.connect(self.listenCommand)

        self.label_7 = QMovie("D:/AI/Real AI/lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        self.label.setPixmap(QPixmap("D:/AI/Real AI/lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>" + self.ts + "</font>")
        self.label_5.setFont(QFont(QFont('Acens', 8)))

        self.Dspeak = mainT()
        self.Dspeak.start()

    def listenCommand(self):
        self.Dspeak.STT()


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())





























