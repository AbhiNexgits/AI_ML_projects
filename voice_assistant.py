from neuralintents import GenericAssistant
import sys
import threading
import tkinter as tk
# from tkinter import *
import speech_recognition
import speech_recognition as sr
import pyttsx3 as tts
import nltk
import webbrowser
import datetime
import wikipedia

nltk.download('omw-1.4')


# class Hello:
#     def __init__(self):
#         self.speak()
#         self.hello()
#     def speak(self,audio):
#         engine = tts.init()
#
#         voices = engine.getProperty('voices')
#
#
#         engine.setProperty('voice', voices[0].id)
#
#         engine.say(audio)
#
#         engine.runAndWait()
#
#     def hello(self,speak):
#         speak.say("hello sir I am your desktop assistant.Tell me how may I help you")
# Hello()

class Assistant:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        voices = self.speaker.getProperty('voices')
        self.speaker.setProperty('voice', voices[1].id)  # use 0 for male voice and use 1 for female voice
        self.speaker.setProperty("rate", 150)
        self.assistant = GenericAssistant("intents.json",
                                          intent_methods={"file": self.create_file, "google": self.google,
                                                          "wikipedia": self.wiki})
        self.assistant.train_model()
        self.root = tk.Tk()
        self.label = tk.Label(text="Abhi's Bot ", font=("Arial", 50, "bold"))
        self.label.pack()
        threading.Thread(target=self.run_assistant).start()

        self.root.mainloop()

    def google(self):
        self.speaker.say("Opening Google")
        webbrowser.open("www.google.com")

    def create_file(self):
        with open("aifile.txt", "w") as f:
            f.write("hello world")

    # def takeCommand(self):
    #     r = sr.Recognizer()
    #
    #     with sr.Microphone() as source:
    #         print('Listening')
    #
    #         r.pause_threshold = 0.7
    #         audio = r.listen(source)
    #         try:
    #             print("Recognizing")
    #
    #             Query = r.recognize_google(audio, language='en-in')
    #             print("the command is printed=", Query)
    #
    #         except Exception as e:
    #             print(e)
    #
    #         return Query

    def wiki(self, audio):
        # audio=self.recognizer.listen(mic)
        query = self.recognizer.recognize_google(audio).lower()
        self.speaker.say("Checking the wikipedia ")
        query = query.replace("wikipedia", "")

        # it will give the summary of 4 lines from
        # wikipedia we can increase and decrease
        # it also.
        result = wikipedia.summary(query, sentences=4)
        self.speaker.say("According to wikipedia")
        self.speaker.say(result)

    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=5) # change duration in seconds for activate bot
                    audio = self.recognizer.listen(mic)
                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()
                    print(text)

                    if "hello siri" in text:
                        self.label.config(fg="green")
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio)
                        print("the command is printed=", text)
                        text = text.lower()
                        if text == "stop":
                            self.speaker.say("Bye ,Check Out nexgits for more exciting things")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            self.root.destroy()
                            sys.exit()
                        else:
                            if text is not None:
                                response = self.assistant.request(text)
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()
                            self.label.config(fg="black")
            except:
                self.label.config(fg="red")
                continue


Assistant()
