# Jarvis - Assistant Personnel IA avec Ollama

Un assistant personnel IA local utilisant **Ollama** et **Mistral** sur une **RTX 3070 8GB**.

## 🚀 Caractéristiques

✅ **Modèles légers** - Compatible RTX 3070 8GB  
✅ **Lancer des applications** - Notepad, Chrome, etc.  
✅ **Calculs mathématiques** - Dérivées, intégrales, résolution d'équations  
✅ **Tâches basiques** - Heure, date, recherche web  
✅ **Communication IA** - Réponses intelligentes via Ollama  
✅ **Interface CLI intuitive**  

## 📋 Pré-requis

- **Ollama** installé et en cours d'exécution ([ollama.ai](https://ollama.ai))
- **Python 3.8+**
- **RTX 3070 8GB** (ou GPU équivalent)

## 📦 Installation

### 1. Démarrer Ollama

```bash
# Vérifiez qu'Ollama est lancé
ollama serve
```

### 2. Télécharger un modèle léger (dans un autre terminal)

**Pour RTX 3070 8GB, recommandé:**
```bash
# Mistral 7B (4-5GB) - Très bon équilibre
ollama pull mistral

# Alternative plus légère (3B)
ollama pull neural-chat
ollama pull dolphin-phi
```

### 3. Installer les dépendances Python

```bash
# Configurez votre environnement Python d'abord
C:/Users/benja/AppData/Local/Python/pythoncore-3.14-64/python.exe -m pip install --upgrade pip

# Installez les dépendances
C:/Users/benja/AppData/Local/Python/pythoncore-3.14-64/python.exe -m pip install -r requirements.txt
```

### 4. Configuration

Copiez `.env.example` en `.env`:
```bash
copy .env.example .env
```

Éditez `.env` si nécessaire:
```env
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=mistral:latest
USE_TTS=False
```

## ▶️ Utilisation

```bash
C:/Users/benja/AppData/Local/Python/pythoncore-3.14-64/python.exe main.py
```

### Exemples de commandes

```
💬 Vous: ouvre notepad
Jarvis: ✓ notepad lancé avec succès

💬 Vous: dérivée x**2 + 3*x
Jarvis: Expression: x**2 + 3*x
        Dérivée: 2*x + 3
        Simplifié: 2*x + 3

💬 Vous: résous x**2 - 4
Jarvis: Solutions: [-2, 2]

💬 Vous: heure
Jarvis: Il est 14:30:45 (24/04/2026)

💬 Vous: recherche meteo marseille
Jarvis: ✓ Recherche lancée pour: meteo marseille

💬 Vous: pourquoi le ciel est bleu?
Jarvis: ⏳ Réflexion...
        [Réponse d'Ollama sur le phénomène de Rayleigh]
```

## 📊 Modèles recommandés

| Modèle | VRAM | Vitesse | Qualité |
|--------|------|---------|---------|
| Mistral 7B | 4-5GB | Rapide | Très bon |
| Neural Chat 7B | 3-4GB | Rapide | Bon |
| Dolphin Phi 3B | 3GB | Très rapide | Bon |
| Orca Mini 3B | 2GB | Très rapide | Acceptable |

## 🔧 Structure du projet

```
Jarvis/
├── main.py                      # Point d'entrée
├── requirements.txt             # Dépendances
├── .env.example                # Configuration d'exemple
└── jarvis/
    ├── config.py               # Configuration
    ├── ollama_connector.py      # Connexion Ollama
    ├── agents/
    │   ├── application_launcher.py  # Lancer des apps
    │   ├── calculator.py            # Calculs math
    │   ├── tasks.py                 # Tâches basiques
    │   └── __init__.py
    └── utils/
        └── __init__.py
```

## 💡 Conseils

- **Modèle**: Commencez par `mistral` (meilleur équilibre)
- **VRAM**: Vérifiez avec `ollama ps` pour voir la consommation
- **Performance**: Ajustez `OLLAMA_MODEL` dans `.env` pour plus/moins de puissance
- **Offline**: Fonctionne complètement hors ligne une fois le modèle téléchargé

## 📝 Notes

- Les réponses de l'IA dépendent de la qualité du modèle
- Pour une meilleure reconnaissance mathématique, utilisez des symboles clairs
- Les tâches système (arrêt, redémarrage) nécessitent les permissions appropriées

## 🐛 Dépannage

**Ollama ne répond pas?**
```bash
# Vérifiez que c'est lancé
ollama serve
```

**Modèle non trouvé?**
```bash
# Téléchargez-le
ollama pull mistral
```

**Erreur de VRAM?**
```bash
# Utilisez un modèle plus léger
ollama pull orca-mini
```

## 📄 Licence

Libre d'utilisation

---

**Créé pour RTX 3070 8GB** 🚀
