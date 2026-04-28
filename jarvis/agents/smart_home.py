"""
🏠 Système de contrôle Smart Home
Contrôle d'appareils connectés (lumières, température, etc.)
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
import os

class SmartHomeDevice:
    """Représente un appareil smart home"""
    
    def __init__(self, name: str, device_type: str, room: str, status: bool = False):
        self.name = name
        self.device_type = device_type  # "lumière", "chauffage", "climatisation", "porte", etc
        self.room = room
        self.status = status  # On/Off
        self.intensity = 100 if device_type == "lumière" else 20  # Pour lumières
        self.temperature = 20 if device_type in ["chauffage", "climatisation"] else None
        self.last_changed = datetime.now()
    
    def toggle(self) -> Dict:
        """Allume/éteint l'appareil"""
        self.status = not self.status
        self.last_changed = datetime.now()
        return {
            "success": True,
            "device": self.name,
            "action": "ON" if self.status else "OFF",
            "message": f"✓ {self.name} est maintenant {'allumé' if self.status else 'éteint'}"
        }
    
    def set_intensity(self, intensity: int) -> Dict:
        """Règle l'intensité (pour les lumières)"""
        if self.device_type != "lumière":
            return {"success": False, "error": "Cet appareil ne supporte pas l'intensité"}
        
        self.intensity = max(0, min(100, intensity))
        self.last_changed = datetime.now()
        return {
            "success": True,
            "device": self.name,
            "intensity": self.intensity,
            "message": f"✓ Intensité de {self.name}: {self.intensity}%"
        }
    
    def set_temperature(self, temp: int) -> Dict:
        """Règle la température"""
        if self.device_type not in ["chauffage", "climatisation"]:
            return {"success": False, "error": "Cet appareil ne gère pas la température"}
        
        self.temperature = max(10, min(30, temp))
        self.last_changed = datetime.now()
        return {
            "success": True,
            "device": self.name,
            "temperature": self.temperature,
            "message": f"✓ Température de {self.name}: {self.temperature}°C"
        }
    
    def to_dict(self) -> Dict:
        """Retourne l'état de l'appareil"""
        return {
            "name": self.name,
            "type": self.device_type,
            "room": self.room,
            "status": "ON" if self.status else "OFF",
            "intensity": self.intensity if self.device_type == "lumière" else None,
            "temperature": self.temperature if self.device_type in ["chauffage", "climatisation"] else None,
            "last_changed": self.last_changed.strftime("%H:%M:%S")
        }


class SmartHome:
    """Gestionnaire du système Smart Home"""
    
    def __init__(self):
        self.devices: Dict[str, SmartHomeDevice] = {}
        self._init_default_devices()
        self.automation_enabled = True
    
    def _init_default_devices(self):
        """Initialise les appareils par défaut"""
        # Salon
        self.add_device("Lumière Salon", "lumière", "Salon")
        self.add_device("Chauffage Salon", "chauffage", "Salon")
        
        # Chambre
        self.add_device("Lumière Chambre", "lumière", "Chambre")
        self.add_device("Chauffage Chambre", "chauffage", "Chambre")
        
        # Cuisine
        self.add_device("Lumière Cuisine", "lumière", "Cuisine")
        self.add_device("Four", "appareil", "Cuisine")
        
        # Salle de bain
        self.add_device("Lumière SdB", "lumière", "Salle de bain")
        self.add_device("Ventilateur SdB", "ventilateur", "Salle de bain")
        
        # Porte d'entrée
        self.add_device("Porte Entrée", "porte", "Entrée")
    
    def add_device(self, name: str, device_type: str, room: str) -> Dict:
        """Ajoute un nouvel appareil"""
        device_id = name.lower().replace(" ", "_")
        
        if device_id in self.devices:
            return {"success": False, "error": f"Appareil {name} existe déjà"}
        
        self.devices[device_id] = SmartHomeDevice(name, device_type, room)
        return {
            "success": True,
            "message": f"✓ Appareil {name} ajouté"
        }
    
    def control_device(self, device_name: str, action: str, value: Optional[int] = None) -> Dict:
        """Contrôle un appareil"""
        device = self._find_device(device_name)
        
        if not device:
            return {"success": False, "error": f"Appareil {device_name} non trouvé"}
        
        action = action.lower()
        
        if action in ["allume", "on", "activé"]:
            device.status = True
            device.last_changed = datetime.now()
            return {
                "success": True,
                "message": f"✓ {device.name} allumé"
            }
        elif action in ["éteint", "off", "désactivé"]:
            device.status = False
            device.last_changed = datetime.now()
            return {
                "success": True,
                "message": f"✓ {device.name} éteint"
            }
        elif action in ["toggle", "bascule"]:
            return device.toggle()
        elif action in ["intensité", "luminosité"] and value is not None:
            return device.set_intensity(value)
        elif action in ["température", "temp"] and value is not None:
            return device.set_temperature(value)
        else:
            return {"success": False, "error": f"Action {action} non supportée"}
    
    def control_room(self, room_name: str, action: str, value: Optional[int] = None) -> Dict:
        """Contrôle tous les appareils d'une pièce"""
        devices_in_room = [d for d in self.devices.values() if d.room == room_name]
        
        if not devices_in_room:
            return {"success": False, "error": f"Pièce {room_name} non trouvée"}
        
        results = []
        for device in devices_in_room:
            result = self.control_device(device.name, action, value)
            if result["success"]:
                results.append(device.name)
        
        return {
            "success": True,
            "room": room_name,
            "affected": results,
            "message": f"✓ {len(results)} appareil(s) contrôlé(s) dans {room_name}"
        }
    
    def _find_device(self, name: str) -> Optional[SmartHomeDevice]:
        """Cherche un appareil par nom"""
        name_lower = name.lower()
        
        # Recherche exacte
        for device_id, device in self.devices.items():
            if device.name.lower() == name_lower:
                return device
        
        # Recherche partielle
        for device_id, device in self.devices.items():
            if name_lower in device.name.lower():
                return device
        
        return None
    
    def get_status(self, filter_room: Optional[str] = None) -> Dict:
        """Récupère le statut de tous les appareils"""
        devices = []
        
        for device in self.devices.values():
            if filter_room is None or device.room == filter_room:
                devices.append(device.to_dict())
        
        # Grouper par pièce
        by_room = {}
        for device in devices:
            room = device["room"]
            if room not in by_room:
                by_room[room] = []
            by_room[room].append(device)
        
        return {
            "total_devices": len(devices),
            "by_room": by_room,
            "devices": devices
        }
    
    def create_scene(self, scene_name: str, config: Dict) -> Dict:
        """Crée une scène (configuration prédéfinie)"""
        scenes_dir = "jarvis/data/scenes"
        os.makedirs(scenes_dir, exist_ok=True)
        
        scene_file = os.path.join(scenes_dir, f"{scene_name}.json")
        
        with open(scene_file, "w") as f:
            json.dump(config, f, indent=2)
        
        return {
            "success": True,
            "message": f"✓ Scène '{scene_name}' créée"
        }
    
    def activate_scene(self, scene_name: str) -> Dict:
        """Active une scène prédéfinie"""
        scenes_dir = "jarvis/data/scenes"
        scene_file = os.path.join(scenes_dir, f"{scene_name}.json")
        
        if not os.path.exists(scene_file):
            return {"success": False, "error": f"Scène '{scene_name}' non trouvée"}
        
        with open(scene_file, "r") as f:
            config = json.load(f)
        
        results = []
        for device_name, state in config.items():
            action = state.get("action", "toggle")
            value = state.get("value")
            result = self.control_device(device_name, action, value)
            if result["success"]:
                results.append(device_name)
        
        return {
            "success": True,
            "scene": scene_name,
            "affected": results,
            "message": f"✓ Scène '{scene_name}' activée"
        }


# Instance globale
smart_home = SmartHome()
