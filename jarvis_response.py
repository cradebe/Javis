import pyttsx3


class Jarvis:
    def __init__(self):
        self.jarvis = pyttsx3.init()
        self.jarvis.setProperty('rate', 160)

    def talk(self, jarvis_response):
        self.jarvis.say(jarvis_response)
        self.jarvis.runAndWait()
