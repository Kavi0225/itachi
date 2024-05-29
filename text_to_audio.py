import pyttsx3 as p
import speech_recognition as sr
# var = "hi"
def texttospeech(var):

    text_speech = p.init()
    # var = input("enter the input : ")

    # getting the voice
    voices = text_speech.getProperty('voices')
    # print(voices)
    # getting the rate of the current speech
    rate = text_speech.getProperty('rate')
    text_speech.setProperty('rate',100)

    # set the volume of the speech
    volume = text_speech.getProperty('volume')
    text_speech.setProperty('volume',100)

    # voices = text_speech.getProperty('voices')
    text_speech.setProperty('voice',voices[1].id)

    text_speech.say(var)
    text_speech.runAndWait()
    text_speech.stop()
# texttospeech(var)


