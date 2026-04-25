import time
import random

def human_delay(text: str = ""):
    base = 0.15
    length_factor = len(text) * 0.003
    randomness = random.uniform(0.05, 0.3)

    time.sleep(base + length_factor + randomness)


def humanize_text(text: str):
    text = text.replace(".", "...")
    text = text.replace(",", ", ")
    return text