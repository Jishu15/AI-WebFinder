import os
import speech_recognition as sr

def say(text):
    print(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en_in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Jarvis AI!")
    print("Listening...")
    text = takeCommand()
    if text:
        say(text)
