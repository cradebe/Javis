import os
import sys
from datetime import datetime

import pywhatkit
import speech_recognition as sr
import ctypes

from pyjokes import pyjokes
from wikipedia import wikipedia

from jarvis_response import Jarvis


def wait_for_wakeup(jarvis_engine):
    user_speech = sr.Recognizer()
    # user_speech.energy_threshold = 300
    mic = sr.Microphone()
    running = True
    while running:
        with mic as source:
            try:
                print("Listening")
                user_speech.adjust_for_ambient_noise(source, duration=0.2)
                jarvis_name = user_speech.listen(source)
                print(user_speech.recognize_google(jarvis_name))
                if 'dude' in user_speech.recognize_google(jarvis_name):
                    jarvis_engine.talk("Yo Dude")
                    running = listening(jarvis_engine, source, user_speech)
                jarvis_name = None

            except sr.UnknownValueError:
                pass
                # jarvis_engine.talk("I like it for the pirates?")
                # print(f'Error: UnknownValueError')
            except sr.WaitTimeoutError:
                print(f'Error: WaitTimeoutError')
            except sr.RequestError:
                print(f'Error: RequestError')


def listening(jarvis_engine, source, user_speech):
    user_speech.adjust_for_ambient_noise(source, duration=0.2)
    print("Listening")
    audio = user_speech.listen(source)
    try:
        command = user_speech.recognize_google(audio)
        command.lower()
        print(command)
        if 'thank you' in command:
            jarvis_engine.talk("Thank you Lulu for your hospitality")
        elif 'lock' in command:
            jarvis_engine.talk("Signing Out")
            print("lock")
            ctypes.windll.user32.LockWorkStation()
            sys.exit()
        elif 'play' in command:
            song = command.replace('play', '')
            jarvis_engine.talk('alright my ninja, I got you. playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.now().strftime('%I:%M %p')
            jarvis_engine.talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            print('here')
            info = wikipedia.summary(person, 1)
            print(info)
            jarvis_engine.talk(info)
        elif 'clean' in command:
            jarvis_engine.talk('Alright you slob, watch me work')
            os.system(r"C:\Users\Colin.Radebe\Desktop\SalaryCollections\myTools\desktop_cleaner_files.py")
        elif 'date' in command:
            jarvis_engine.talk('sorry, I have a headache')
        elif 'are you single' in command:
            jarvis_engine.talk('I am in a relationship with wifi')
        elif 'joke' in command:
            jarvis_engine.talk(pyjokes.get_joke())
        elif 'analysis' in command:
            jarvis_engine.talk('running facial analysis')
            os.system(r"C:\Users\Colin.Radebe\Desktop\NCR\NB\pudi\deep_face_project\deep_face_project.py")
        # else:
        #     jarvis_engine.talk('Please say the command again.')
        else:
            jarvis_engine.talk("I don't have a response for that yet. I am still learning, Please try something else or speak a little bit clearer")
            listening(jarvis_engine, source, user_speech)

    except sr.UnknownValueError:
        jarvis_engine.talk("I didn't understand that")
        print("Listening")
        listening(jarvis_engine, source, user_speech)
    finally:
        return True


if __name__ == "__main__":
    jarvis_engine = Jarvis()
    wait_for_wakeup(jarvis_engine)
