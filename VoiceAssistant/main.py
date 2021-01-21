
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'baymax' in command:
                command = command.replace('baymax', '')

    except:
        pass
    return command


def run_baymax():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing '+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)


run_baymax()
