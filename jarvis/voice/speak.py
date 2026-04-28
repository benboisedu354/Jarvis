import edge_tts
import tempfile
import asyncio
import threading
from jarvis.voice.human import human_delay, humanize_text
from jarvis.voice.audio import audio_engine

VOICE = "fr-FR-HenriNeural"


def _run_speech(text):
    try:
        text = humanize_text(text)
        human_delay(text)

        file_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name

        async def generate():
            communicate = edge_tts.Communicate(text, VOICE)
            await communicate.save(file_path)

        asyncio.run(generate())

        audio_engine.play(file_path)

    except Exception as e:
        print("TTS error:", e)


def speak(text):
    print("🤖 Jarvis:", text)

    threading.Thread(target=_run_speech, args=(text,), daemon=True).start()