import pyautogui
from io import BytesIO
import base64

def capture_screen_base64():
    """
    Capture l'écran et le convertit en base64
    """
    screenshot = pyautogui.screenshot()

    buffer = BytesIO()
    screenshot.save(buffer, format="PNG")

    return base64.b64encode(buffer.getvalue()).decode("utf-8")