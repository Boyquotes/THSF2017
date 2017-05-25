import pyttsx
engine = pyttsx.init()

voices = engine.getProperty('voices')
engine.setProperty('rate', 70)

engine.setProperty('voices', voices[4])
engine.say("coucou")
engine.runAndWait()
