#
#
# voice.py
# Author -> GoldenDuck5 (github)
# Code Parsing and Refactoring -> TheVigilante51 (github)
#
#

import pyttsx3

# Initialize Text-to-Speech
text_to_speech_engine = pyttsx3.init()
text_to_speech_engine.setProperty('rate', 150)
text_to_speech_engine.setProperty('volume', 1.0)

#Speak Function to speak a given text
def speak(text):
    print(f"assistant: {text}")
    text_to_speech_engine.say(text)
    text_to_speech_engine.runAndWait()
