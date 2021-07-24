# import os
# import time
# import playsound
# import speech_recognition as sr
# from gtts import gTTS
#
# def speak(text):
#     tts = gTTS(text=text, lang="en")
#     filename = "voice.mp3"
#     tts.save(filename)
#     playsound.playsound(filename)
#
# speak("hello world")0

import json
import requests
from win32com.client import Dispatch


def Speak(string):
    speak = Dispatch("SAPI.spVoice")
    speak.Speak(string)


if __name__ == '__main__':
    Speak("News for today....Lets Begin")
    News_url = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=95a2058faa4e49ddb1391a8fcc2de3eb").text
    News_dict = json.loads(News_url)
    print(News_dict["articles"])
    arts = News_dict['articles']
    for article in arts:
        Speak(article['title'])
        Speak("Moving on to the next news ... ")

    Speak("Thanks for Listening.")
