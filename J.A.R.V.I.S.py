import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup
import pytz
from pywinauto.application import Application
from tkinter import *
import datetime
import time
import winsound
from threading import *
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
converter = pyttsx3.init()
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
converter.setProperty('rate', 50)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Evening!")
        speak("Good Afternoon!")






def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        speak(f"you said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
        return "exit"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)
            speak(results)

        elif 'open youtube' in query:
            speak('sure sir')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('sure sir')
            webbrowser.open("google.com")

        elif 'hello' in query:
            speak('hi sir')

        elif 'how are you' in query:
            speak('im fine sir')

        elif 'what is my age' in query:
            speak('your age is 17 sir')

        elif 'when is my birthday' in query:
            speak('sir,your birthday is on december 8th')

        elif 'open whatsapp' in query:
            speak('sure')
            webbrowser.open('web.whatsapp.com')

        elif 'play buddha song' in query:
            speak('sure')
            webbrowser.open('https://www.youtube.com/watch?v=6JPc0OlvuOM')

        elif 'what is the time' in query:
            current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            speak("The current time in india is : ")
            speak(current_time)

        elif 'thank you' in query:
            speak('it is my pleasure sir!!')
            exit()
        elif 'play music' in query:
            speak('sure playing...')
            music_dir = 'E:\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'open spotify' in query:
            speak('sure sir')
            os.system("spotify")
        elif 'open file explorer' in query:
            speak('sure opening sir..')
            os.system('explorer')
        elif 'open notepad' in query:
            speak('opening sir..')
            os.system('notepad')








