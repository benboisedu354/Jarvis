"""
💾 Système de mémoire Jarvis
Apprend et se souvient des préférences et informations utilisateur
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class JarvisMemory:
    """Gère la mémoire persistante de Jarvis"""
    
    def __init__(self, data_dir: str = "jarvis/data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        
        self.memory_file = os.path.join(data_dir, "memory.json")
        self.preferences_file = os.path.join(data_dir, "preferences.json")
        self.learning_file = os.path.join(data_dir, "learning.json")
        
        self.memory = self._load_json(self.memory_file)
        self.preferences = self._load_json(self.preferences_file)
        self.learning = self._load_json(self.learning_file)
    
    def _load_json(self, filepath: str) -> Dict:
        """Charge un fichier JSON"""
        if os.path.exists(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                pass
        return {}
    
    def _save_json(self, filepath: str, data: Dict):
        """Sauvegarde un fichier JSON"""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    # MÉMOIRE PERSONNELLE
    def store_personal_info(self, key: str, value: str) -> Dict:
        """Stocke une info personnelle"""
        if "personal" not in self.memory:
            self.memory["personal"] = {}
        
        self.memory["personal"][key] = {
            "value": value,
            "timestamp": datetime.now().isoformat()
        }
        self._save_json(self.memory_file, self.memory)
        
        return {
            "success": True,
            "message": f"✓ Info stockée: {key}"
        }
    
    def get_personal_info(self, key: str) -> Optional[str]:
        """Récupère une info personnelle"""
        if "personal" in self.memory and key in self.memory["personal"]:
            return self.memory["personal"][key]["value"]
        return None
    
    # PRÉFÉRENCES
    def set_preference(self, category: str, key: str, value: str) -> Dict:
        """Définit une préférence"""
        if category not in self.preferences:
            self.preferences[category] = {}
        
        self.preferences[category][key] = value
        self._save_json(self.preferences_file, self.preferences)
        
        return {
            "success": True,
            "message": f"✓ Préférence sauvegardée: {category}/{key}"
        }
    
    def get_preference(self, category: str, key: str) -> Optional[str]:
        """Récupère une préférence"""
        if category in self.preferences and key in self.preferences[category]:
            return self.preferences[category][key]
        return None
    
    # HISTORIQUE D'APPRENTISSAGE
    def record_interaction(self, user_input: str, response: str, success: bool = True) -> Dict:
        """Enregistre une interaction avec l'utilisateur"""
        if "interactions" not in self.learning:
            self.learning["interactions"] = []
        
        self.learning["interactions"].append({
            "user_input": user_input,
            "response": response,
            "success": success,
            "timestamp": datetime.now().isoformat()
        })
        
        # Garder seulement les 1000 dernières interactions
        if len(self.learning["interactions"]) > 1000:
            self.learning["interactions"] = self.learning["interactions"][-1000:]
        
        self._save_json(self.learning_file, self.learning)
        
        return {
            "success": True,
            "interactions_count": len(self.learning["interactions"])
        }
    
    def get_interaction_stats(self) -> Dict:
        """Retourne les stats d'interactions"""
        if "interactions" not in self.learning:
            return {"total": 0, "successful": 0, "success_rate": 0}
        
        interactions = self.learning["interactions"]
        total = len(interactions)
        successful = sum(1 for i in interactions if i.get("success", True))
        success_rate = (successful / total * 100) if total > 0 else 0
        
        return {
            "total": total,
            "successful": successful,
            "success_rate": round(success_rate, 2),
            "failure_rate": round(100 - success_rate, 2)
        }
    
    # CONTEXTE UTILISATEUR
    def learn_habit(self, habit: str, frequency: str) -> Dict:
        """Apprend une habitude de l'utilisateur"""
        if "habits" not in self.learning:
            self.learning["habits"] = {}
        
        self.learning["habits"][habit] = {
            "frequency": frequency,
            "learned_at": datetime.now().isoformat()
        }
        self._save_json(self.learning_file, self.learning)
        
        return {
            "success": True,
            "message": f"✓ Habitude mémorisée: {habit} ({frequency})"
        }
    
    def get_habits(self) -> Dict:
        """Récupère les habitudes apprises"""
        return self.learning.get("habits", {})
    
    # CONTACTS ET RELATIONS
    def save_contact(self, name: str, info: Dict) -> Dict:
        """Sauvegarde un contact"""
        if "contacts" not in self.memory:
            self.memory["contacts"] = {}
        
        self.memory["contacts"][name.lower()] = {
            **info,
            "added_at": datetime.now().isoformat()
        }
        self._save_json(self.memory_file, self.memory)
        
        return {
            "success": True,
            "message": f"✓ Contact sauvegardé: {name}"
        }
    
    def get_contact(self, name: str) -> Optional[Dict]:
        """Récupère les infos d'un contact"""
        if "contacts" in self.memory:
            return self.memory["contacts"].get(name.lower())
        return None
    
    # RÉSUMÉ DE LA MÉMOIRE
    def get_memory_summary(self) -> Dict:
        """Résumé de ce que Jarvis se souvient"""
        personal_keys = len(self.memory.get("personal", {}))
        contacts = len(self.memory.get("contacts", {}))
        preferences_count = sum(len(v) for v in self.preferences.values())
        habits = len(self.learning.get("habits", {}))
        
        return {
            "personal_info": personal_keys,
            "contacts": contacts,
            "preferences": preferences_count,
            "habits": habits,
            "interactions": len(self.learning.get("interactions", [])),
            "memory_used_mb": os.path.getsize(self.memory_file) / (1024**2) if os.path.exists(self.memory_file) else 0
        }
    
    def display_memory_content(self):
        """Affiche le résumé et le contenu formaté de la mémoire"""
        summary = self.get_memory_summary()
        print(f"""
╔════════════════════════════════════════════════════════════════╗
║                   💾 MÉMOIRE JARVIS                           ║
╚════════════════════════════════════════════════════════════════╝

📊 STATISTIQUES:
  📝 Infos personnelles: {summary['personal_info']}
  👥 Contacts: {summary['contacts']}
  ⚙️  Préférences: {summary['preferences']}
  🎯 Habitudes: {summary['habits']}
  📊 Interactions: {summary['interactions']}
  💾 Espace mémoire: {summary['memory_used_mb']:.2f} MB

════════════════════════════════════════════════════════════════
""")
        
        # AFFICHAGE FORMATÉ DE LA MÉMOIRE
        if self.memory.get("personal"):
            print("\n📋 INFOS PERSONNELLES:")
            for key, data in self.memory["personal"].items():
                print(f"   • {key}: {data['value']}")
        
        if self.memory.get("goals"):
            print("\n🎯 OBJECTIFS:")
            for key, data in self.memory["goals"].items():
                print(f"   • {key}: {data['value']}")
        
        if self.memory.get("contacts"):
            print("\n👥 CONTACTS:")
            for name, contact_data in self.memory["contacts"].items():
                print(f"   • {name}:")
                for k, v in contact_data.items():
                    if k != "added_at":
                        print(f"      - {k}: {v}")
        
        if self.learning.get("habits"):
            print("\n🎯 HABITUDES:")
            for habit, info in self.learning["habits"].items():
                print(f"   • {habit}: {info.get('frequency', 'N/A')}")
        
        if self.preferences:
            print("\n⚙️  PRÉFÉRENCES:")
            for category, prefs in self.preferences.items():
                print(f"   [{category}]")
                for key, value in prefs.items():
                    print(f"      • {key}: {value}")
        
        print("\n════════════════════════════════════════════════════════════════\n")
    
    def print_memory_summary(self):
        """Affiche le contenu complet de la mémoire"""
        return self.display_memory_content()


# Instance globale
memory = JarvisMemory()
