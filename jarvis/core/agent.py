from jarvis.core.browser import browser

def run_agent(text: str):
    text = text.lower()

    if "netflix" in text:
        browser.open("https://www.netflix.com")
        return "Netflix ouvert"

    if "youtube" in text:
        browser.open("https://www.youtube.com")
        return "YouTube ouvert"

    if "google" in text:
        browser.open("https://www.google.com")
        return "Google ouvert"

    if "kill netflix" in text:
        browser.close_tab("netflix")
        return "Netflix fermé"

    if "kill youtube" in text:
        browser.close_tab("youtube")
        return "YouTube fermé"

    if "kill tout" in text:
        browser.close_all()
        return "Toutes les fenêtres fermées"

    return None