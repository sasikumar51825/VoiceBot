import pyttsx3

def speak(text):
    """Speak the given text"""
    engine = pyttsx3.init()  # initialize every time
    engine.say(text)
    engine.runAndWait()
    engine.stop()  # ensure engine is released
