from jarvis.core.brain import ask_llm
from jarvis.audio.tts import speak
from jarvis.audio.stt import listen_micro
from jarvis.core.state import state
from jarvis.voice.loop import run_voice_loop

def main():
    print("🤖 Jarvis démarré")
    state.running = True
    state.active = False
    # Je veux que Jarvis soit actif uniquement quand je lui parle, pas besoin de dire "Jarvis" à chaque fois

    while state.running:
        try:
            text = listen_micro()

            if not text:
                continue

            text = text.lower()

            # 🛑 ARRÊT COMPLET
            if "arrêt jarvis" in text or "arret jarvis" in text or "stop jarvis" in text:
                speak("Arrêt du système. À bientôt.")
                state.running = False
                state.active = False
                break
            


        except KeyboardInterrupt:
            print("\nArrêt clavier détecté")
            state.running = False
            state.active = False
            break


        except Exception as e:
            print("Erreur:", e)


if __name__ == "__main__":
    main()