from jarvis.core.browser import browser
from jarvis.agents.agenda import agenda
from jarvis.agents.personality import personality
from jarvis.agents.smart_home import smart_home
from jarvis.agents.dashboard import dashboard
from jarvis.agents.memory import memory
from jarvis.agents.priority import priority_manager
import re
from datetime import datetime, timedelta


OPEN_WORDS = ["ouvre", "lance", "mets", "démarre", "go", "affiche"]
CLOSE_WORDS = ["ferme", "quitte", "stop", "enlève"]

SITES = {
    "netflix": "https://www.netflix.com",
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "twitch": "https://www.twitch.tv"
}


def detect_action(text: str):
    for word in OPEN_WORDS:
        if word in text:
            return "open"

    for word in CLOSE_WORDS:
        if word in text:
            return "close"

    return None


def detect_site(text: str):
    for site in SITES:
        if site in text:
            return site
    return None


def run_agent(text: str):
    text = text.lower()

    # =====================
    # 📅 AGENDA
    # =====================

    # ➕ Ajouter
    if any(word in text for word in ["ajoute", "ajouter", "créer", "crée", "planifier", "planifie"]):
        result = parse_and_add_event(text)
        if result:
            return result

    # 📋 Lister
    if any(word in text for word in ["agenda", "calendrier", "aujourd", "today", "semaine"]):
        if "aujourd" in text or "today" in text:
            result = agenda.lister_evenements_aujourd_hui()
        elif "semaine" in text:
            result = agenda.obtenir_evenements_semaine()
        else:
            result = agenda.lister_evenements(limite=10)

        if result.get("events"):
            events_str = "\n".join([
                f"• {e['titre']} - {e['date']} {e.get('heure', '')}"
                for e in result.get("events", [])
            ])
            return f"Voici votre agenda:\n{events_str}"

        return result.get("message", "Pas d'événements")

    # ❌ Supprimer
    if any(word in text for word in ["supprime", "efface", "retire"]):
        match = re.search(r'\d+', text)
        if match:
            return agenda.supprimer_evenement(int(match.group())).get("message")

    # ✅ Compléter
    if any(word in text for word in ["fait", "terminé", "complete"]):
        match = re.search(r'\d+', text)
        if match:
            return agenda.marquer_complete(int(match.group())).get("message")

    # =====================
    # 🌐 BROWSER
    # =====================

    action = detect_action(text)
    site = detect_site(text)

    if action == "open" and site:
        browser.open(SITES[site])
        return f"{site.capitalize()} ouvert"

    if action == "close" and site:
        browser.close_tab(site)
        return f"{site.capitalize()} fermé"

    # =====================
    # 🏠 SMART HOME
    # =====================

    # Lancer commandes smart home
    if any(word in text for word in ["lumière", "lumiere", "chauffage", "climatisation", "appliance", "appareil"]):
        
        # Allumer/Éteindre
        if any(word in text for word in ["allume", "on", "active", "active"]):
            # Trouver le device
            for device_name in smart_home.devices.values():
                if device_name.name.lower() in text:
                    return smart_home.control_device(device_name.name, "on").get("message", "")
        
        # Éteindre
        if any(word in text for word in ["éteint", "eteint", "off", "désactive", "desactive"]):
            for device_name in smart_home.devices.values():
                if device_name.name.lower() in text:
                    return smart_home.control_device(device_name.name, "off").get("message", "")
        
        # Intensité
        if "intensité" in text or "intensite" in text or "luminosité" in text or "luminosite" in text:
            match = re.search(r'(\d+)%?', text)
            if match:
                intensity = int(match.group(1))
                for device_name in smart_home.devices.values():
                    if device_name.name.lower() in text:
                        return smart_home.control_device(device_name.name, "intensité", intensity).get("message", "")
        
        # Température
        if "température" in text or "temperature" in text or "chaud" in text:
            match = re.search(r'(\d+)', text)
            if match:
                temp = int(match.group(1))
                for device_name in smart_home.devices.values():
                    if device_name.name.lower() in text:
                        return smart_home.control_device(device_name.name, "température", temp).get("message", "")
    
    # Statut maison
    if any(word in text for word in ["statut", "status", "état", "etat", "maison"]):
        status = smart_home.get_status()
        response = f"🏠 État de la maison:\n"
        for room, devices in status["by_room"].items():
            response += f"\n{room}:\n"
            for device in devices:
                status_str = "🟢 ON" if device["status"] == "ON" else "🔴 OFF"
                response += f"  • {device['name']}: {status_str}\n"
        return response

    # =====================
    # ⚡ PRIORITÉS & TÂCHES
    # =====================

    # Ajouter une tâche
    if any(word in text for word in ["ajoute tâche", "ajoute tache", "ajouter tâche", "ajouter tache", "créer tâche", "créer tache"]):
        # Extraire titre et priorité
        title_match = re.search(r'(?:tâche|tache)\s+(.+?)(?:\s+(?:urgent|critique|élevée|elevee|normale|faible)|$)', text)
        priority = "MEDIUM"
        
        if "urgent" in text or "critique" in text:
            priority = "HIGH"
        elif "critique" in text:
            priority = "CRITICAL"
        elif "faible" in text:
            priority = "LOW"
        
        if title_match:
            title = title_match.group(1).strip()
            result = priority_manager.add_task(title, priority)
            return result.get("message", "")
    
    # Lister tâches
    if any(word in text for word in ["mes tâches", "mes taches", "liste tâches", "liste taches", "tâches"]):
        summary = priority_manager.get_daily_summary()
        return summary
    
    # Compléter une tâche
    if any(word in text for word in ["complète", "complete", "termine", "terminé", "fait"]):
        match = re.search(r'(?:tâche|tache)\s+(.+)', text)
        if match:
            task_title = match.group(1).strip()
            result = priority_manager.complete_task(task_title)
            return result.get("message", "")

    # =====================
    # 📊 DASHBOARD
    # =====================

    # Afficher le dashboard
    if any(word in text for word in ["dashboard", "résumé", "resume", "statut", "status", "infos"]):
        if "complet" in text or "full" in text:
            dashboard.print_dashboard()
            return "📊 Dashboard complet affiché"
        else:
            return dashboard.get_brief_summary()

    # =====================
    # 💾 MÉMOIRE
    # =====================

    # Stocker une info perso
    if any(word in text for word in ["me rappelle", "me souvenir", "je m'appelle", "je suis"]):
        # Format: "mon nom est Jean", "je suis développeur", etc
        match = re.search(r'(?:je suis|je m\'appelle|mon nom est)\s+(.+)', text)
        if match:
            info = match.group(1).strip()
            # Extraire type d'info
            if "appelle" in text or "nom" in text:
                memory.store_personal_info("name", info)
                return f"✓ Je me souviendrai que vous êtes {info}"
            elif "suis" in text:
                memory.store_personal_info("profession", info)
                return f"✓ Noté: vous êtes {info}"
    
    # Afficher la mémoire
    if any(word in text for word in ["ma mémoire", "ma memoire", "souviens-toi", "souviens"]):
        memory.print_memory_summary()
        return 

    # =====================
    # 🤖 PERSONNALITÉ
    # =====================

    # Greetings et répliques personnalisées
    if "salut" in text or "bonjour" in text or "bonsoir" in text:
        return personality.get_greeting()
    
    if "merci" in text or "thanks" in text:
        return personality.respond_to_thanks()
    
    if any(word in text for word in ["bravo", "excellent", "super", "compliment"]):
        return personality.respond_to_compliment()
    
    # Répliques sarcastiques pour demandes impossibles
    if any(word in text for word in ["vole", "teleporte", "magie", "impossible"]):
        return personality.get_sarcastic_reply()

    return None


# =====================
# 🧠 PARSER AGENDA
# =====================

def parse_and_add_event(text: str):
    try:
        title_match = re.search(
            r'(?:ajoute|ajouter|créer|crée|planifie)\s+(.+?)(?:\s+(?:demain|aujourd|\d{1,2}/\d{1,2}|à)|$)',
            text
        )

        if not title_match:
            return None

        titre = title_match.group(1).strip()

        # 📅 Date
        if "demain" in text:
            date_str = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        else:
            date_str = datetime.now().strftime("%d/%m/%Y")

        # ⏰ Heure
        heure = None
        time_match = re.search(r'(\d{1,2})[h:](\d{0,2})', text)
        if time_match:
            h = time_match.group(1)
            m = time_match.group(2) or "00"
            heure = f"{h}:{m}"

        result = agenda.ajouter_evenement(
            titre=titre[:50],
            date=date_str,
            heure=heure,
            rappel=True
        )

        return result.get("message", "Événement ajouté")

    except Exception as e:
        return f"Erreur: {e}"