#!/usr/bin/env python3
"""
Jarvis - Assistant Personnel IA
Utilise Ollama avec un modèle local sur RTX 3070 8GB
"""

import sys
import re
from jarvis.ollama_connector import OllamaConnector
from jarvis.agents import ApplicationLauncher, Calculator, TaskHandler
from jarvis.config import OLLAMA_HOST, OLLAMA_MODEL, USE_TTS

# Initialisation des agents
ollama = OllamaConnector()
app_launcher = ApplicationLauncher()
calculator = Calculator()
task_handler = TaskHandler()

def check_ollama():
    """Vérifie la connexion à Ollama"""
    print("🔍 Vérification de la connexion Ollama...")
    if ollama.check_connection():
        models = ollama.get_available_models()
        print(f"✓ Ollama connecté sur {OLLAMA_HOST}")
        print(f"✓ Modèle utilisé: {OLLAMA_MODEL}")
        print(f"✓ Modèles disponibles: {', '.join(models)}\n")
        return True
    else:
        print(f"✗ Impossible de se connecter à Ollama sur {OLLAMA_HOST}")
        print("   Assurez-vous qu'Ollama est lancé: ollama serve\n")
        return False

def process_command(user_input: str):
    """Traite les commandes de l'utilisateur"""
    user_input = user_input.strip()
    
    if not user_input:
        return
    
    # Commandes système
    if user_input.lower() in ["quit", "exit", "quitter", "sortir"]:
        print("Au revoir! 👋")
        sys.exit(0)
    
    if user_input.lower() in ["help", "aide", "?"]:
        print_help()
        return
    
    # Ouvrir une application
    if user_input.lower().startswith(("ouvre ", "lance ", "open ", "start ")):
        app_name = user_input[6:].strip()
        result = app_launcher.launch_app(app_name)
        print(result["message"])
        return
    
    # Calculs mathématiques
    if user_input.lower().startswith(("dérivée ", "derivee ", "derivative ")):
        expr = user_input.split(" ", 1)[1]
        result = calculator.derivative(expr)
        if result["success"]:
            print(f"Expression: {result['expression']}")
            print(f"Dérivée: {result['derivative']}")
            print(f"Simplifié: {result['simplified']}")
        else:
            print(f"Erreur: {result['error']}")
        return
    
    if user_input.lower().startswith(("intégrale ", "integrale ", "integral ")):
        expr = user_input.split(" ", 1)[1]
        result = calculator.integral(expr)
        if result["success"]:
            print(f"Expression: {result['expression']}")
            print(f"Intégrale: {result['integral']}")
            print(f"Simplifié: {result['simplified']}")
        else:
            print(f"Erreur: {result['error']}")
        return
    
    if user_input.lower().startswith(("résous ", "resous ", "solve ")):
        expr = user_input.split(" ", 1)[1]
        result = calculator.solve_equation(expr)
        if result["success"]:
            print(f"Équation: {result['equation']}")
            print(f"Solutions: {result['solutions']}")
        else:
            print(f"Erreur: {result['error']}")
        return
    
    if user_input.lower().startswith(("calcule ", "calculate ")):
        expr = user_input.split(" ", 1)[1]
        result = calculator.calculate(expr)
        if result["success"]:
            print(f"Expression: {result['expression']}")
            print(f"Résultat: {result['result']}")
            if result["decimal"]:
                print(f"Décimal: {result['decimal']:.6f}")
        else:
            print(f"Erreur: {result['error']}")
        return
    
    # Tâches basiques
    if user_input.lower() in ["heure", "quelle heure", "time"]:
        time_info = task_handler.get_time()
        print(f"Il est {time_info['time']} ({time_info['date']})")
        return
    
    if user_input.lower() in ["date", "quelle date", "today"]:
        date_info = task_handler.get_date()
        print(f"Aujourd'hui: {date_info['date']} ({date_info['day']})")
        return
    
    if user_input.lower().startswith(("recherche ", "search ", "cherche ")):
        query = user_input.split(" ", 1)[1]
        result = task_handler.search_web(query)
        print(result["message"])
        return
    
    if user_input.lower().startswith(("ouvre site ", "open site ")):
        url = user_input.split(" ", 2)[2]
        result = task_handler.open_website(url)
        print(result["message"])
        return
    
    # Commandes d'arrêt/redémarrage
    if user_input.lower() in ["arrête", "arrête pc", "shutdown"]:
        result = task_handler.shutdown_pc()
        print(result["message"])
        return
    
    if user_input.lower() in ["redémarre", "redémarre pc", "restart"]:
        result = task_handler.restart_pc()
        print(result["message"])
        return
    
    # Communication avec le modèle IA pour autres questions
    print("⏳ Réflexion...", end=" ", flush=True)
    prompt = f"""Tu es Jarvis, un assistant personnel IA courtois et utile.
Réponds de manière concise et en français.
L'utilisateur dit: {user_input}"""
    
    response = ollama.generate_response(prompt)
    print("\r" + " " * 30 + "\r")  # Efface "⏳ Réflexion..."
    print(f"Jarvis: {response}\n")

def print_help():
    """Affiche l'aide"""
    help_text = """
╔════════════════════════════════════════════════════════════════╗
║                    JARVIS - Guide d'utilisation                ║
╚════════════════════════════════════════════════════════════════╝

🎯 APPLICATIONS:
  • ouvre [application]    → Lance une application
    Ex: ouvre notepad, ouvre chrome, ouvre calculatrice

📐 CALCULS MATHÉMATIQUES:
  • calcule [expression]   → Évalue une expression
    Ex: calcule 2+3*4, calcule sqrt(16)
  • dérivée [expression]   → Calcule la dérivée
    Ex: dérivée x**2 + 3*x
  • intégrale [expression] → Calcule l'intégrale
    Ex: intégrale x**2
  • résous [équation]      → Résout une équation
    Ex: résous x**2 - 4 = 0

⏰ TÂCHES BASIQUES:
  • heure                  → Affiche l'heure
  • date                   → Affiche la date
  • recherche [terme]      → Recherche sur Google
    Ex: recherche météo Marseille
  • ouvre site [url]       → Ouvre un site web
    Ex: ouvre site google.com

🔋 CONTRÔLE SYSTÈME:
  • arrête                 → Éteint le PC
  • redémarre              → Redémarre le PC

❓ AUTRES:
  • [n'importe quelle question] → Ollama répondra
  • help                   → Affiche cette aide
  • quit                   → Quitte Jarvis

╔════════════════════════════════════════════════════════════════╗
"""
    print(help_text)

def main():
    """Boucle principale"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║                    🤖 JARVIS - Assistant IA 🤖               ║
║                  Motorisé par Ollama + Mistral                 ║
╚════════════════════════════════════════════════════════════════╝
    """)
    
    if not check_ollama():
        print("⚠️  Démarrez Ollama avant de continuer:")
        print("   ollama serve")
        sys.exit(1)
    
    print_help()
    
    while True:
        try:
            user_input = input("\n💬 Vous: ").strip()
            if user_input:
                process_command(user_input)
        except KeyboardInterrupt:
            print("\n\nAu revoir! 👋")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    main()
