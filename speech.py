import speech_recognition as sr
from sas import *
import pyttsx3 as p

r = sr.Recognizer()
def speak(command):

    engine = p.init()
    engine.say(command)
    engine.runAndWait()
def to_speak():
    try:
        print("please speak")
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2 , duration= 0.2)
            mytext = p.init()
            audio2 = r.listen(source2)
            mytext = r.recognize_google(audio2)
            mytext = mytext.lower()
            print("Did you say ",mytext)
            speak(mytext)

            saswords = text_synonym_antonym(mytext)
            print(saswords)

    except sr.RequestError as e:
        print("Could not request; {0}".format(e))

    except sr.UnknownValueError:
        print("error")
    return saswords
# to_speak()