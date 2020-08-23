import os
from gtts import gTTS
from playsound import playsound

Text = "I love Django central and Python programming Language"

print("please wait...processing")
TTS = gTTS(text=Text, lang='en-uk')

# Save to mp3 in current dir.
TTS.save("voice.mp3")

# Plays the mp3 using the default app on your system
# that is linked to mp3s.
playsound("voice.mp3")

# # import speech
# # speech.say('Hola mundo', 'es_ES')

# import pyttsx
# engine = pyttsx.init()
# engine.say('Good morning.')
# engine.runAndWait()