# 🎯 JARVIS - Vue d'ensemble du projet

## 📊 Structure complète

```
c:\Users\benja\Documents\Dev\Jarvis\
│
├─ 📋 FICHIERS DE CONFIGURATION
│  ├─ .env                     Configuration active (Ollama + modèle)
│  ├─ .env.example             Exemple de configuration
│  └─ requirements.txt         Dépendances Python (requests, sympy, etc)
│
├─ 📖 DOCUMENTATION
│  ├─ README.md                Documentation complète (complet)
│  ├─ DEMARRAGE_RAPIDE.md      Démarrage en 3 étapes (À LIRE D'ABORD!)
│  ├─ GUIDE_MODELES.md         Recommandations modèles Ollama
│  ├─ DEVELOPPEMENT.md         Guide pour étendre Jarvis
│  ├─ CHECKLIST.md             Checklist avant utilisation
│  ├─ INSTALLATION_COMPLETE.txt Résumé de l'installation
│  └─ PROJET.md                Ce fichier
│
├─ 🚀 SCRIPTS DE LANCEMENT
│  ├─ jarvis.bat               LANCEUR PRINCIPAL (double-cliquez)
│  └─ installer_modeles.bat    Installation facile des modèles
│
├─ 💾 CODE PRINCIPAL
│  ├─ main.py                  Point d'entrée (CLI interactive)
│  │
│  └─ jarvis/                  Package principal
│     ├─ __init__.py
│     ├─ config.py             Configuration globale
│     ├─ ollama_connector.py    Client Ollama
│     │
│     ├─ agents/               Modules de fonctionnalités
│     │  ├─ __init__.py
│     │  ├─ application_launcher.py  [Lancer apps Windows]
│     │  ├─ calculator.py            [Calculs math: dérivée, intégrale...]
│     │  ├─ tasks.py                 [Tâches: heure, date, recherche web]
│     │  └─ [À étendre avec vos agents]
│     │
│     └─ utils/                Utilitaires
│        └─ __init__.py        [À étendre]
│
└─ 🔧 AUTRES
   └─ .venv/                   Environnement virtuel (généré automatiquement)
```

---

## 🎯 Flux d'utilisation

```
┌─────────────────────────────────────────────────────────────────┐
│                      USER (Vous)                                │
└────────────────────────┬────────────────────────────────────────┘
                         │
                    Double-cliquez
                    jarvis.bat
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      main.py                                    │
│            (Boucle interactive CLI)                             │
│  Lit les commandes utilisateur et les traite                    │
└────────┬──────────────────┬──────────────────────┬──────────────┘
         │                  │                      │
         ▼                  ▼                      ▼
    ┌─────────┐      ┌──────────┐         ┌──────────────┐
    │ Agents  │      │ Agents   │         │ Agents       │
    │         │      │          │         │              │
    │ App     │      │Calc      │         │Tasks         │
    │Launcher │      │Math      │         │              │
    │         │      │          │         │- Heure/Date  │
    │ .launch │      │.derive   │         │- Recherche   │
    │  _app() │      │.integral │         │- Web browser │
    │         │      │.solve()  │         │- Arrêt/Init  │
    └────┬────┘      └────┬─────┘         └──────┬───────┘
         │                │                      │
         ▼                ▼                      ▼
    Exécute            Calcule            Tâche système
    (subprocess)       (Sympy)            (webbrowser,
                                           datetime, etc)
         │
         │  Si question générale ou non reconnue:
         │
         ▼
    ┌──────────────────────────────────────┐
    │  ollama_connector                    │
    │                                      │
    │  connect → http://localhost:11434    │
    │  send    → prompt utilisateur        │
    │  receive → réponse du modèle         │
    │                                      │
    │  Modèles:                            │
    │  - Mistral 7B (recommandé)           │
    │  - Neural Chat                       │
    │  - Dolphin Phi                       │
    │  - Orca Mini                         │
    └──────────────────────────────────────┘
         │
         ▼
    ┌──────────────────────────────────────┐
    │  Ollama Server                       │
    │  (localhost:11434)                   │
    │                                      │
    │  Charge modèle dans GPU              │
    │  Génère réponse                      │
    │  Retourne texte                      │
    └──────────────────────────────────────┘
         │
         ▼
    Affiche réponse à l'utilisateur
```

---

## 🔌 Connexions externes

```
┌─────────────────┐
│ Jarvis (Python) │
└────────┬────────┘
         │
    ┌────┴────────────────┬────────────────┬─────────────────┐
    │                     │                │                 │
    ▼                     ▼                ▼                 ▼
┌────────────┐    ┌─────────────┐   ┌───────────┐   ┌─────────────┐
│ Ollama API │    │Windows Cmd  │   │ Sympy     │   │ webbrowser  │
│            │    │(subprocess) │   │ (Python)  │   │ (stdlib)    │
│ POST /api/ │    │             │   │           │   │             │
│ generate   │    │ subprocess  │   │ compute   │   │ open URL    │
│            │    │ .Popen()    │   │ math      │   │             │
│ Port 11434 │    │             │   │           │   │             │
└────────────┘    └─────────────┘   └───────────┘   └─────────────┘
```

---

## 🚀 Modèles Ollama disponibles

```
┌──────────────────────────────────────────────────────────────────┐
│                    Espace GPU RTX 3070 8GB                       │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────────────────────┐  VRAM libre: ~3GB     │
│  │    MISTRAL 7B (Recommandé)          │  ⭐⭐⭐⭐⭐             │
│  │    Poids: 4-5GB (Chargé)           │  Vitesse: ⚡⚡        │
│  │                                     │  Qualité: Excellente  │
│  │    MEILLEUR ÉQUILIBRE                │                      │
│  └─────────────────────────────────────┘                        │
│                                                                  │
│  Alternatives possibles:                                        │
│  - Neural Chat 7B (3-4GB) - Plus léger                         │
│  - Dolphin Phi 3B (3GB) - Encore plus léger                    │
│  - Orca Mini 3B (2GB) - Très léger                             │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 💾 Flux de données

```
USER INPUT
    │
    ▼
"ouvre chrome"  ──► [agents/application_launcher.py]
                    subprocess.Popen("chrome.exe")
                    │
                    └─► Chrome s'ouvre
                         Retour: {"success": True}
                    
"dérivée x**2"  ──► [agents/calculator.py]
                    sympy.diff(x**2, x)
                    │
                    └─► Calcule 2*x
                         Retour: {"derivative": "2*x"}

"quelle heure?" ──► [agents/tasks.py]
                    datetime.datetime.now()
                    │
                    └─► "14:30:45"
                         Retour: {"time": "14:30:45"}

"Pourquoi le ciel?" ──► [ollama_connector.py]
                       POST http://localhost:11434/api/generate
                       │
                       ▼
                    [Ollama + Mistral]
                    │
                    └─► "Le ciel est bleu car..."
```

---

## 🔧 Configuration files

### `.env` (Active)
```
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=mistral:latest
USE_TTS=False
```

### `config.py` (Code)
```python
OLLAMA_HOST = "http://localhost:11434"
OLLAMA_MODEL = "mistral:latest"
USE_TTS = False
```

### `.venv/` (Virtualenv)
```
Contient:
- Python 3.14.4
- requests, sympy, pyttsx3, python-dotenv
```

---

## 🎯 Dépendances

```
Python 3.14.4
├─ requests (2.31.0)           → Requêtes HTTP vers Ollama
├─ sympy (1.12)                → Calculs mathématiques symboliques
├─ pyttsx3 (2.90)              → Synthèse vocale (optionnel)
├─ python-dotenv (1.0.0)       → Variables d'environnement (.env)
└─ pyautogui (0.9.53) [optionnel] → Contrôle souris/clavier
```

---

## 🚀 Flux de démarrage

```
1. Double-cliquez jarvis.bat
   │
   ├─► jarvis.bat (batch file)
   │   ├─► affiche intro
   │   ├─► lance main.py via Python
   │   │
   │   └─► Charge:
   │       ├─ .env
   │       ├─ config.py
   │       ├─ OllamaConnector
   │       ├─ ApplicationLauncher
   │       ├─ Calculator
   │       └─ TaskHandler
   │
   ├─► main.py démarre
   │   ├─► vérifie Ollama
   │   ├─► affiche aide
   │   └─► boucle interactive
   │
   └─► Prêt à recevoir commandes
```

---

## 📝 Exemple d'ajout d'agent

```
1. Créer jarvis/agents/weather.py
   class WeatherAgent: ...

2. Importer dans jarvis/agents/__init__.py
   from .weather import WeatherAgent

3. Utiliser dans main.py
   weather = WeatherAgent()
   if "météo" in user_input:
       result = weather.get_weather(...)

4. Tester
   python main.py
```

---

## 🎓 Points d'entrée

### Point d'entrée principal
```
jarvis.bat  →  main.py  →  processus interactif
```

### Point d'entrée alternatif
```
PowerShell  →  python main.py  →  processus interactif
```

### Point d'entrée installation
```
installer_modeles.bat  →  Interface menu  →  ollama pull
```

---

## 📊 État du projet

✅ **Fonctionnalités complètes:**
- [x] CLI interactive
- [x] Connexion Ollama
- [x] Lancer applications
- [x] Calculs mathématiques
- [x] Tâches basiques
- [x] Communication IA
- [x] Configuration .env
- [x] Documentation complète
- [x] Scripts de démarrage
- [x] Checklist

⏳ **À améliorer (optionnel):**
- [ ] Interface GUI (tkinter/PyQt)
- [ ] Reconnaissance vocale
- [ ] Synthèse vocale
- [ ] Cache des réponses
- [ ] Historique de chat
- [ ] Plugins système
- [ ] API REST

---

## 📞 Support

1. **Erreur technique?** → Consultez DEMARRAGE_RAPIDE.md
2. **Question modèles?** → Consultez GUIDE_MODELES.md
3. **Veux développer?** → Consultez DEVELOPPEMENT.md
4. **Besoin de checklist?** → Consultez CHECKLIST.md

---

## ✨ Résumé rapide

- **Qu'est-ce?** Assistant IA local avec Ollama
- **Pourquoi?** Privé, offline, optimisé pour RTX 3070 8GB
- **Comment?** Double-cliquez jarvis.bat
- **Quoi faire?** Taper des commandes
- **Modèle?** Mistral 7B (recommandé)

---

*Jarvis v1.0 - Créé 24/04/2026*
*Optimisé pour RTX 3070 8GB*
