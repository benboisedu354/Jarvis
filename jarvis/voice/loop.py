from jarvis.voice.listen import listen
from jarvis.voice.speak import speak
from jarvis.core.brain import ask_llm
from jarvis.core.state import state

WAKE_WORD = "jarvis"


def run_voice_loop():
    print("🎧 Jarvis démarré")

    while state.running:

        text = listen()

        if not text:
            continue

        text = text.lower()

        # 🛑 ARRÊT COMPLET SYSTEME
        if "arrêt jarvis" in text or "arret jarvis" in text or "stop jarvis" in text:
            speak("Arrêt du système. À bientôt.")
            state.running = False
            state.active = False
            break

        # 😴 veille
        if "veille" in text:
            state.active = False
            speak("Mode veille activé")
            continue

        # 🔔 wake word
        if WAKE_WORD in text:
            state.active = True
            speak("Oui ?")
            continue

        if not state.active:
            continue

        response = ask_llm(text)

        if response:
            speak(response)

    print("🛑 Jarvis complètement arrêté")