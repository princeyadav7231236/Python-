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


News_url = requests.get(
    "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=95a2058faa4e49ddb1391a8fcc2de3eb",
    params={"status": "ok", "id": "the-times-of-india",
            "name": "The Times of India"}
)
var1 = dict[News_url]
json_news_file = News_url.json()
if __name__ == '__main__':
    # Speak("You are my first assistant")
    print(News_url.text)
    print(json_news_file)
    Speak(json_news_file)
