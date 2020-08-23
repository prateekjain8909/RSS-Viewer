import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak :")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    # print("joijjoi")

try:
    text = r.recognize_google(audio)

    print(text)

except Exception as e:

    print(e)
    print("Voice is not clear")