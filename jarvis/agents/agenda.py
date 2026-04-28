"""Agent pour la gestion de l'agenda virtuel"""
import sqlite3
import os
from datetime import datetime, timedelta
from typing import Dict, List

DB_PATH = "data/memory.db"

class AgendaHandler:
    """Gère l'agenda virtuel avec persistance en base de données"""
    
    def __init__(self):
        self.init_db()
    
    def init_db(self):
        """Initialise la table d'agenda si elle n'existe pas"""
        os.makedirs("data", exist_ok=True)
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        c.execute("""
            CREATE TABLE IF NOT EXISTS agenda (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT NOT NULL,
                description TEXT,
                date TEXT NOT NULL,
                heure TEXT,
                rappel INTEGER DEFAULT 0,
                completed INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
    
    def ajouter_evenement(self, titre: str, date: str, heure: str = None, description: str = None, rappel: bool = True) -> Dict:
        """Ajoute un événement à l'agenda"""
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            
            # Validation de la date (format DD/MM/YYYY ou YYYY-MM-DD)
            try:
                if "/" in date:
                    datetime.strptime(date, "%d/%m/%Y")
                else:
                    datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                return {
                    "success": False,
                    "message": f"Format de date invalide. Utilisez JJ/MM/AAAA ou AAAA-MM-JJ"
                }
            
            rappel_int = 1 if rappel else 0
            
            c.execute("""
                INSERT INTO agenda (titre, description, date, heure, rappel)
                VALUES (?, ?, ?, ?, ?)
            """, (titre, description, date, heure, rappel_int))
            
            conn.commit()
            conn.close()
            
            return {
                "success": True,
                "message": f"✓ Événement '{titre}' ajouté au {date}" + (f" à {heure}" if heure else "")
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"✗ Erreur: {e}"
            }
    
    def lister_evenements(self, limite: int = None) -> Dict:
        """Liste tous les événements à venir"""
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            
            query = "SELECT id, titre, date, heure, description, completed FROM agenda WHERE completed = 0 ORDER BY date ASC"
            
            if limite:
                query += f" LIMIT {limite}"
            
            c.execute(query)
            events = c.fetchall()
            conn.close()
            
            if not events:
                return {
                    "success": True,
                    "events": [],
                    "message": "Aucun événement prévu"
                }
            
            formatted_events = []
            for event_id, titre, date, heure, description, completed in events:
                formatted_events.append({
                    "id": event_id,
                    "titre": titre,
                    "date": date,
                    "heure": heure or "Toute la journée",
                    "description": description or "—",
                    "statut": "✓" if completed else "○"
                })
            
            return {
                "success": True,
                "events": formatted_events,
                "count": len(formatted_events)
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"✗ Erreur: {e}"
            }
    
    def lister_evenements_aujourd_hui(self) -> Dict:
        """Liste les événements d'aujourd'hui"""
        try:
            today = datetime.now().strftime("%d/%m/%Y")
            
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            
            c.execute("""
                SELECT id, titre, heure, description FROM agenda 
                WHERE date = ? AND completed = 0 
                ORDER BY heure ASC
            """, (today,))
            
            events = c.fetchall()
            conn.close()
            
            if not events:
                return {
                    "success": True,
                    "events": [],
                    "message": "Aucun événement prévu aujourd'hui"
                }
            
            formatted_events = [
                {
                    "id": e[0],
                    "titre": e[1],
                    "heure": e[2] or "Toute la journée",
                    "description": e[3] or "—"
                }
                for e in events
            ]
            
            return {
                "success": True,
                "events": formatted_events,
                "count": len(formatted_events),
                "message": f"Vous avez {len(formatted_events)} événement(s) aujourd'hui"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"✗ Erreur: {e}"
            }
    
    def supprimer_evenement(self, event_id: int) -> Dict:
        """Supprime un événement"""
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            
            # Récupérer le titre avant de supprimer
            c.execute("SELECT titre FROM agenda WHERE id = ?", (event_id,))
            result = c.fetchone()
            
            if not result:
                conn.close()
                return {
                    "success": False,
                    "message": f"Événement ID {event_id} non trouvé"
                }
            
            titre = result[0]
            c.execute("DELETE FROM agenda WHERE id = ?", (event_id,))
            
            conn.commit()
            conn.close()
            
            return {
                "success": True,
                "message": f"✓ Événement '{titre}' supprimé"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"✗ Erreur: {e}"
            }
    
    def marquer_complete(self, event_id: int) -> Dict:
        """Marque un événement comme complété"""
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            
            # Récupérer le titre
            c.execute("SELECT titre FROM agenda WHERE id = ?", (event_id,))
            result = c.fetchone()
            
            if not result:
                conn.close()
                return {
                    "success": False,
                    "message": f"Événement ID {event_id} non trouvé"
                }
            
            titre = result[0]
            c.execute("UPDATE agenda SET completed = 1 WHERE id = ?", (event_id,))
            
            conn.commit()
            conn.close()
            
            return {
                "success": True,
                "message": f"✓ '{titre}' marqué comme complété"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"✗ Erreur: {e}"
            }
    
    def modifier_evenement(self, event_id: int, **kwargs) -> Dict:
        """Modifie un événement existant"""
        try:
            allowed_fields = {"titre", "description", "date", "heure", "rappel"}
            fields_to_update = {k: v for k, v in kwargs.items() if k in allowed_fields}
            
            if not fields_to_update:
                return {
                    "success": False,
                    "message": "Aucun champ valide à modifier"
                }
            
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            
            # Vérifier que l'événement existe
            c.execute("SELECT titre FROM agenda WHERE id = ?", (event_id,))
            result = c.fetchone()
            
            if not result:
                conn.close()
                return {
                    "success": False,
                    "message": f"Événement ID {event_id} non trouvé"
                }
            
            # Construire la requête UPDATE dynamiquement
            set_clause = ", ".join([f"{field} = ?" for field in fields_to_update.keys()])
            values = list(fields_to_update.values()) + [event_id]
            
            c.execute(f"UPDATE agenda SET {set_clause} WHERE id = ?", values)
            
            conn.commit()
            conn.close()
            
            return {
                "success": True,
                "message": f"✓ Événement '{result[0]}' modifié"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"✗ Erreur: {e}"
            }
    
    def obtenir_evenements_semaine(self) -> Dict:
        """Liste les événements de la semaine"""
        try:
            today = datetime.now()
            events_by_day = {}
            
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            
            for i in range(7):
                day = today + timedelta(days=i)
                date_str = day.strftime("%d/%m/%Y")
                day_name = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"][day.weekday()]
                
                c.execute("""
                    SELECT titre, heure FROM agenda 
                    WHERE date = ? AND completed = 0 
                    ORDER BY heure ASC
                """, (date_str,))
                
                events = c.fetchall()
                if events:
                    events_by_day[f"{day_name} {date_str}"] = [
                        f"• {e[0]} à {e[1]}" if e[1] else f"• {e[0]}"
                        for e in events
                    ]
            
            conn.close()
            
            return {
                "success": True,
                "events": events_by_day,
                "message": "Agenda de la semaine"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"✗ Erreur: {e}"
            }
    
    def nettoyer_evenements_passes(self) -> Dict:
        """Supprime les événements complétés et passés"""
        try:
            yesterday = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y")
            
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            
            c.execute("DELETE FROM agenda WHERE date < ? AND completed = 1", (yesterday,))
            
            deleted = c.rowcount
            conn.commit()
            conn.close()
            
            return {
                "success": True,
                "message": f"✓ {deleted} événement(s) archivé(s)"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"✗ Erreur: {e}"
            }


# Instance globale
agenda = AgendaHandler()
