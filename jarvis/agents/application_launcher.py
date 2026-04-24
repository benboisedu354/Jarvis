"""Agent pour lancer des applications"""
import subprocess
import os
import re
from typing import List, Dict

class ApplicationLauncher:
    """Lance les applications sur Windows"""
    
    # Chemins courants pour les applications
    APP_PATHS = {
        "notepad": "notepad.exe",
        "calculatrice": "calc.exe",
        "calc": "calc.exe",
        "calculator": "calc.exe",
        "explorateur": "explorer.exe",
        "file explorer": "explorer.exe",
        "explorer": "explorer.exe",
        "cmd": "cmd.exe",
        "powershell": "powershell.exe",
        "paint": "mspaint.exe",
        "wordpad": "wordpad.exe",
        "tâches": "taskmgr.exe",
        "task manager": "taskmgr.exe",
        "settings": "ms-settings:",
        "paramètres": "ms-settings:",
    }
    
    # Applications courantes dans Program Files
    COMMON_APPS = {
        "chrome": ["Google\\Chrome\\Application\\chrome.exe", "Chromium\\Application\\chrome.exe"],
        "firefox": ["Mozilla Firefox\\firefox.exe"],
        "vs code": ["Microsoft VS Code\\Code.exe"],
        "vscode": ["Microsoft VS Code\\Code.exe"],
        "spotify": ["Spotify\\Spotify.exe"],
        "discord": ["Discord\\Discord.exe"],
        "vlc": ["VideoLAN\\VLC\\vlc.exe"],
        "7zip": ["7-Zip\\7zFM.exe"],
    }
    
    def launch_app(self, app_name: str) -> Dict[str, str]:
        """Lance une application"""
        app_name_lower = app_name.lower().strip()
        
        # Cherche dans APP_PATHS
        if app_name_lower in self.APP_PATHS:
            path = self.APP_PATHS[app_name_lower]
            try:
                subprocess.Popen(path, shell=True)
                return {
                    "success": True,
                    "message": f"✓ {app_name} lancé avec succès"
                }
            except Exception as e:
                return {
                    "success": False,
                    "message": f"✗ Erreur lors du lancement de {app_name}: {e}"
                }
        
        # Cherche dans Program Files
        program_files = os.environ.get("ProgramFiles", "C:\\Program Files")
        program_files_x86 = os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)")
        
        for app_key, paths in self.COMMON_APPS.items():
            if app_key in app_name_lower:
                for relative_path in paths:
                    for base_path in [program_files, program_files_x86]:
                        full_path = os.path.join(base_path, relative_path)
                        if os.path.exists(full_path):
                            try:
                                subprocess.Popen(full_path)
                                return {
                                    "success": True,
                                    "message": f"✓ {app_name} lancé avec succès"
                                }
                            except Exception as e:
                                return {
                                    "success": False,
                                    "message": f"✗ Erreur: {e}"
                                }
        
        # Cherche par fichier
        try:
            subprocess.Popen(app_name, shell=True)
            return {
                "success": True,
                "message": f"✓ {app_name} lancé"
            }
        except:
            return {
                "success": False,
                "message": f"✗ Application '{app_name}' non trouvée"
            }
    
    def list_installed_apps(self) -> List[str]:
        """Liste les applications disponibles"""
        apps = list(self.APP_PATHS.keys()) + list(self.COMMON_APPS.keys())
        return sorted(set(apps))
