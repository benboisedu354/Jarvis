import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_micro():
    try:
        print("🎤 En écoute...")

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio, language="fr-FR")

        print(f"👤 Vous: {text}")
        return text.lower()

    except sr.UnknownValueError:
        return None

    except Exception as e:
        print(f"❌ STT error: {e}")
        return None