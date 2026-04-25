import pygame

pygame.mixer.init()


class AudioEngine:
    def __init__(self):
        self.currently_playing = False

    def play(self, file_path):
        try:
            self.currently_playing = True
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                continue

            self.currently_playing = False

        except Exception as e:
            print("Audio error:", e)

    def stop(self):
        pygame.mixer.music.stop()
        self.currently_playing = False


# 🔥 instance globale (Jarvis service)
audio_engine = AudioEngine()