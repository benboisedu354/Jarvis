import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 180)

def speak(text):
    try:
        print(f"🤖 Jarvis: {text}")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"❌ TTS error: {e}")