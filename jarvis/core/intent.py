def detect_intent(text: str):
    text = text.lower()

    if any(k in text for k in ["ouvre", "lance", "open"]):
        return "action"

    if any(k in text for k in ["calcule", "+", "-", "*", "/"]):
        return "math"

    if any(k in text for k in ["explique", "comment", "pourquoi"]):
        return "explain"

    return "chat"