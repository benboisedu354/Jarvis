import webbrowser
import subprocess
import os
import time
import sys

class BrowserController:
    def __init__(self):
        """
        Initialise le contrôleur pour utiliser Firefox existant (pas une nouvelle instance).
        Utilise webbrowser qui se connecte directement à Firefox.
        """
        self.opened_urls = []
        # Essayer de trouver le chemin Firefox
        self.firefox_path = self._find_firefox()


    def _open_firefox_navigator(self):
        """Ouvre Firefox en mode navigateur (si possible)"""
        try:
            if self.firefox_path:
                subprocess.Popen([self.firefox_path, "-new-window"])
                return "✓ Firefox ouvert en mode navigateur"
            else:
                webbrowser.open("https://www.mozilla.org/fr/firefox/new/")
                return "✓ Firefox non trouvé, ouvert la page de téléchargement"
        except Exception as e:
            return f"✗ Erreur: {e}"
    
    def _find_firefox(self):
        """Trouve le chemin d'installation de Firefox"""
        if sys.platform == "win32":
            possible_paths = [
                os.path.expandvars(r"%ProgramFiles%\Mozilla Firefox\firefox.exe"),
                os.path.expandvars(r"%ProgramFiles(x86)%\Mozilla Firefox\firefox.exe"),
                os.path.expandvars(r"%LOCALAPPDATA%\Programs\Firefox\firefox.exe"),
            ]
            for path in possible_paths:
                if os.path.exists(path):
                    return path
        return None

    def open(self, url: str):
        """Ouvre une URL dans Firefox (navigateur existant)"""
        try:
            # Si Firefox est installé, on le force pour ouvrir l'URL
            if self.firefox_path:
                # Ouvrir dans une nouvelle tab du Firefox existant
                subprocess.Popen([self.firefox_path, "-new-tab", url])
            else:
                # Sinon, utiliser le navigateur par défaut du système
                webbrowser.open(url)
            
            self.opened_urls.append(url)
            return f"✓ Ouvert dans Firefox: {url}"
        except Exception as e:
            return f"✗ Erreur: {e}"

    def find_tab(self, keyword: str):
        """Cherche une URL contenant le mot-clé"""
        keyword = keyword.lower()
        for url in self.opened_urls:
            if keyword in url.lower():
                return url
        return None

    def close_tab(self, keyword: str):
        """Marque un tab comme fermé (dans la logique locale)"""
        keyword = keyword.lower()
        for url in self.opened_urls:
            if keyword in url.lower():
                self.opened_urls.remove(url)
                return f"✓ Tab '{keyword}' marqué comme fermé"
        return f"✗ Aucun tab '{keyword}'"

    def close_all(self):
        """Ferme tous les onglets Firefox"""
        try:
            if self.firefox_path:
                # Fermer l'instance Firefox
                subprocess.Popen(["taskkill", "/IM", "firefox.exe", "/F"], 
                               stdout=subprocess.DEVNULL, 
                               stderr=subprocess.DEVNULL)
            self.opened_urls = []
            return "✓ Tous les onglets fermés"
        except Exception as e:
            return f"✗ Erreur: {e}"


# 🔥 INSTANCE EXPORTÉE - Utilise Firefox directement
browser = BrowserController()