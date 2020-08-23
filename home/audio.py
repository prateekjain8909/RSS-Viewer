from gtts import gTTS
from playsound import playsound

Text = """Welcome to RSS Viewer Online. Select the website whose
RSS feed you want to see."""

TTS = gTTS(text=Text, lang='en-uk')

TTS.save("voice.mp3")
playsound("voice.mp3")