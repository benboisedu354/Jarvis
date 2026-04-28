"""
⚡ Système de gestion des priorités
Gère les tâches urgentes vs normales
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
from enum import Enum
import json
import os

class Priority(Enum):
    """Niveaux de priorité"""
    CRITICAL = 1  # 🔴 Critique
    HIGH = 2      # 🟠 Urgent
    MEDIUM = 3    # 🟡 Normal
    LOW = 4       # 🟢 Faible

class Task:
    """Représente une tâche"""
    
    def __init__(self, title: str, priority: Priority, due_date: Optional[datetime] = None):
        self.id = str(datetime.now().timestamp())
        self.title = title
        self.priority = priority
        self.created_at = datetime.now()
        self.due_date = due_date
        self.completed = False
        self.completed_at = None
    
    def mark_completed(self) -> Dict:
        """Marque la tâche comme complétée"""
        self.completed = True
        self.completed_at = datetime.now()
        return {
            "success": True,
            "message": f"✓ Tâche complétée: {self.title}"
        }
    
    def get_urgency(self) -> str:
        """Calcule l'urgence"""
        if self.completed:
            return "✓ Complétée"
        
        if not self.due_date:
            return "📅 Pas de limite"
        
        time_left = self.due_date - datetime.now()
        
        if time_left.total_seconds() < 0:
            return "🔴 RETARD!"
        elif time_left.total_seconds() < 3600:  # < 1 heure
            return "🔴 URGENT!"
        elif time_left.total_seconds() < 86400:  # < 24h
            return "🟠 Urgent"
        else:
            return f"📅 {time_left.days}j"
    
    def to_dict(self) -> Dict:
        """Convertit en dictionnaire"""
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority.name,
            "created_at": self.created_at.isoformat(),
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "completed": self.completed,
            "urgency": self.get_urgency()
        }


class PriorityManager:
    """Gère le système de priorités"""
    
    def __init__(self, data_dir: str = "jarvis/data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        self.tasks_file = os.path.join(data_dir, "tasks.json")
        self.tasks: Dict[str, Task] = {}
        self._load_tasks()
    
    def _load_tasks(self):
        """Charge les tâches depuis le fichier"""
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # Reconstituer les objets Task
                    for task_id, task_data in data.items():
                        task = Task(
                            task_data["title"],
                            Priority[task_data["priority"]],
                            datetime.fromisoformat(task_data["due_date"]) if task_data.get("due_date") else None
                        )
                        task.id = task_id
                        task.completed = task_data["completed"]
                        self.tasks[task_id] = task
            except Exception as e:
                print(f"Erreur chargement tâches: {e}")
    
    def _save_tasks(self):
        """Sauvegarde les tâches"""
        data = {task_id: task.to_dict() for task_id, task in self.tasks.items()}
        with open(self.tasks_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def add_task(self, title: str, priority: str = "MEDIUM", due_hours: Optional[int] = None) -> Dict:
        """Ajoute une nouvelle tâche"""
        try:
            priority_enum = Priority[priority.upper()]
        except KeyError:
            return {"success": False, "error": f"Priorité invalide: {priority}"}
        
        due_date = None
        if due_hours:
            due_date = datetime.now() + timedelta(hours=due_hours)
        
        task = Task(title, priority_enum, due_date)
        self.tasks[task.id] = task
        self._save_tasks()
        
        return {
            "success": True,
            "message": f"✓ Tâche ajoutée: {title}",
            "priority": priority_enum.name,
            "urgency": task.get_urgency()
        }
    
    def complete_task(self, title_or_id: str) -> Dict:
        """Marque une tâche comme complétée"""
        task = self._find_task(title_or_id)
        
        if not task:
            return {"success": False, "error": f"Tâche non trouvée: {title_or_id}"}
        
        task.mark_completed()
        self._save_tasks()
        
        return {
            "success": True,
            "message": f"✓ Tâche complétée: {task.title}"
        }
    
    def _find_task(self, identifier: str) -> Optional[Task]:
        """Cherche une tâche par ID ou titre"""
        # Recherche par ID
        if identifier in self.tasks:
            return self.tasks[identifier]
        
        # Recherche par titre (partielle)
        identifier_lower = identifier.lower()
        for task in self.tasks.values():
            if identifier_lower in task.title.lower():
                return task
        
        return None
    
    def get_critical_tasks(self) -> List[Task]:
        """Retourne les tâches critiques/urgentes"""
        critical = []
        for task in self.tasks.values():
            if not task.completed and task.priority in [Priority.CRITICAL, Priority.HIGH]:
                critical.append(task)
        
        # Trier par urgence
        critical.sort(key=lambda t: (t.priority.value, t.due_date or datetime.max))
        return critical
    
    def get_urgent_reminder(self) -> Optional[str]:
        """Retourne un rappel s'il y a des tâches urgentes"""
        critical = self.get_critical_tasks()
        
        if not critical:
            return None
        
        task = critical[0]
        urgency = task.get_urgency()
        
        messages = {
            "🔴 URGENT!": f"Sir, vous avez une tâche critique: {task.title}",
            "🔴 RETARD!": f"Sir, vous êtes en retard sur: {task.title}",
            "🟠 Urgent": f"Sir, rappel: {task.title} approche",
        }
        
        for key, msg in messages.items():
            if key in urgency:
                return msg
        
        return None
    
    def get_daily_summary(self) -> str:
        """Résumé des tâches du jour"""
        today_tasks = [
            t for t in self.tasks.values()
            if not t.completed and t.due_date
            and t.due_date.date() == datetime.now().date()
        ]
        
        if not today_tasks:
            return "✓ Aucune tâche pour aujourd'hui."
        
        summary = f"📋 Tâches pour aujourd'hui ({len(today_tasks)}):\n"
        
        for task in sorted(today_tasks, key=lambda t: t.priority.value):
            summary += f"  • [{task.priority.name}] {task.title}\n"
        
        return summary
    
    def get_all_tasks(self, include_completed: bool = False) -> List[Dict]:
        """Retourne toutes les tâches"""
        tasks = []
        for task in self.tasks.values():
            if not include_completed and task.completed:
                continue
            tasks.append(task.to_dict())
        
        # Trier par priorité
        tasks.sort(key=lambda t: Priority[t["priority"]].value)
        return tasks
    
    def print_tasks(self, include_completed: bool = False):
        """Affiche les tâches dans la console"""
        tasks = self.get_all_tasks(include_completed)
        
        if not tasks:
            print("Aucune tâche")
            return
        
        print("""
╔════════════════════════════════════════════════════════════════╗
║                   ⚡ MES TÂCHES                               ║
╚════════════════════════════════════════════════════════════════╝
""")
        
        for task in tasks:
            status = "✓" if task["completed"] else " "
            priority_emoji = {
                "CRITICAL": "🔴",
                "HIGH": "🟠",
                "MEDIUM": "🟡",
                "LOW": "🟢"
            }.get(task["priority"], "")
            
            print(f"[{status}] {priority_emoji} {task['title']} ({task['urgency']})")


# Instance globale
priority_manager = PriorityManager()
