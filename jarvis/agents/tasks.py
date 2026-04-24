"""Agent pour les tâches basiques"""
import subprocess
import webbrowser
import os
from datetime import datetime
from typing import Dict

class TaskHandler:
    """Gère les tâches basiques"""
    
    def search_web(self, query: str) -> Dict[str, str]:
        """Ouvre une recherche web"""
        try:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            return {
                "success": True,
                "message": f"✓ Recherche lancée pour: {query}"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"✗ Erreur: {e}"
            }
    
    def open_website(self, url: str) -> Dict[str, str]:
        """Ouvre un site web"""
        try:
            if not url.startswith(("http://", "https://")):
                url = "https://" + url
            webbrowser.open(url)
            return {
                "success": True,
                "message": f"✓ Site ouvert: {url}"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"✗ Erreur: {e}"
            }
    
    def get_time(self) -> Dict[str, str]:
        """Retourne l'heure actuelle"""
        now = datetime.now()
        return {
            "time": now.strftime("%H:%M:%S"),
            "date": now.strftime("%d/%m/%Y"),
            "full": now.strftime("%d/%m/%Y à %H:%M:%S")
        }
    
    def get_date(self) -> Dict[str, str]:
        """Retourne la date actuelle"""
        now = datetime.now()
        return {
            "date": now.strftime("%d/%m/%Y"),
            "day": now.strftime("%A"),
            "month": now.strftime("%B"),
            "year": now.strftime("%Y")
        }
    
    def shutdown_pc(self, delay_seconds: int = 0) -> Dict[str, str]:
        """Éteint le PC"""
        try:
            if delay_seconds > 0:
                cmd = f"shutdown /s /t {delay_seconds}"
                message = f"Arrêt prévu dans {delay_seconds} secondes"
            else:
                cmd = "shutdown /s /t 0"
                message = "Arrêt immédiat"
            
            subprocess.Popen(cmd, shell=True)
            return {
                "success": True,
                "message": f"✓ {message}"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"✗ Erreur: {e}"
            }
    
    def restart_pc(self, delay_seconds: int = 0) -> Dict[str, str]:
        """Redémarre le PC"""
        try:
            if delay_seconds > 0:
                cmd = f"shutdown /r /t {delay_seconds}"
                message = f"Redémarrage prévu dans {delay_seconds} secondes"
            else:
                cmd = "shutdown /r /t 0"
                message = "Redémarrage immédiat"
            
            subprocess.Popen(cmd, shell=True)
            return {
                "success": True,
                "message": f"✓ {message}"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"✗ Erreur: {e}"
            }
    
    def cancel_shutdown(self) -> Dict[str, str]:
        """Annule l'arrêt programmé"""
        try:
            subprocess.Popen("shutdown /a", shell=True)
            return {
                "success": True,
                "message": "✓ Arrêt annulé"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"✗ Erreur: {e}"
            }
