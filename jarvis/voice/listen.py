import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen():
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

        text = recognizer.recognize_google(audio, language="fr-FR")
        print("🎤 User:", text)
        return text.lower()

    except:
        return None

if __name__ == "__main__":
    while True:
        listen()