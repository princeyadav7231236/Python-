import pyttsx3
import pip
import speech_recognition as sr

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

engine.setProperty("rate", voices[1].id)

def speak(audio):

    engine.say(audio)

    engine.runAndWait()


def takeCommand():

    listener = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening.......")

        listener.pause_threshold = 1

        listener.energy_threshold = 400  # This will listen to the louder voice only, so all you need to do is to speak loudly to give the command.

        audio = listener.listen(source, timeout=1, phrase_time_limit=10)  # It will give you ten seconds to give the argument otherwise it will run again

        try:

            print("Recognising.....")

            query = listener.recognize_google(audio, language="en-in")  # Here you can choose the language of your choice

            print(f"User said --> {query} \n")

        except Exception as e:

            # print(e)

            print("Sorry i didn't recognise. Please say it again.....")

            return "None"

        return query

if __name__ == '__main__':

    speak("Hello boss, How're you?")

    # while True:
    #
    #     takeCommand()
