# 🛠️ Guide de développement - Étendre Jarvis

## 📁 Structure du projet

```
Jarvis/
├── main.py                      # Point d'entrée principal
├── jarvis.bat                   # Lanceur (double-cliquez)
├── installer_modeles.bat        # Installation des modèles
├── requirements.txt             # Dépendances Python
├── .env                         # Configuration (créé automatiquement)
├── .env.example                 # Exemple de configuration
├── README.md                    # Documentation complète
├── DEMARRAGE_RAPIDE.md         # Guide de démarrage
├── GUIDE_MODELES.md            # Guide des modèles
│
└── jarvis/
    ├── __init__.py             # Package
    ├── config.py               # Configuration globale
    ├── ollama_connector.py      # Connexion à Ollama
    ├── agents/                 # Agents/Capabilities
    │   ├── __init__.py
    │   ├── application_launcher.py  # Lancer des applications
    │   ├── calculator.py           # Calculs mathématiques
    │   └── tasks.py                # Tâches basiques
    └── utils/
        └── __init__.py
```

---

## 🎯 Comment ajouter une nouvelle capacité

### Exemple: Ajouter un agent "Weather" (Météo)

#### Étape 1: Créer le fichier `jarvis/agents/weather.py`

```python
"""Agent pour la météo"""
import requests
from typing import Dict

class WeatherAgent:
    """Récupère les informations météorologiques"""
    
    def __init__(self):
        self.api_url = "https://api.open-meteo.com/v1/forecast"
    
    def get_weather(self, city: str) -> Dict[str, str]:
        """Récupère la météo pour une ville"""
        try:
            # Exemple simplifié
            return {
                "success": True,
                "city": city,
                "temp": "18°C",
                "condition": "Partiellement nuageux"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
```

#### Étape 2: Mettre à jour `jarvis/agents/__init__.py`

```python
"""Agents pour Jarvis"""
from .application_launcher import ApplicationLauncher
from .calculator import Calculator
from .tasks import TaskHandler
from .weather import WeatherAgent  # ← Ajouter cette ligne

__all__ = ["ApplicationLauncher", "Calculator", "TaskHandler", "WeatherAgent"]
```

#### Étape 3: Ajouter la commande dans `main.py`

```python
# Dans la fonction main(), après les autres imports:
from jarvis.agents import ApplicationLauncher, Calculator, TaskHandler, WeatherAgent

# Dans la fonction main():
weather = WeatherAgent()

# Dans process_command(), ajouter:
if user_input.lower().startswith(("météo ", "weather ")):
    city = user_input.split(" ", 1)[1]
    result = weather.get_weather(city)
    if result["success"]:
        print(f"📍 {result['city']}")
        print(f"🌡️ Température: {result['temp']}")
        print(f"☁️ Condition: {result['condition']}")
    else:
        print(f"Erreur: {result['error']}")
    return
```

---

## 📝 Ajouter un nouveau calcul mathématique

Éditez `jarvis/agents/calculator.py` et ajoutez une méthode:

```python
def taylor_series(self, expression: str, variable: str = "x", n: int = 5) -> Dict[str, str]:
    """Calcule la série de Taylor"""
    try:
        var = symbols(variable)
        expr = parse_expr(expression, transformations=self.transformations, local_dict={variable: var})
        
        series_result = series(expr, var, 0, n)
        
        return {
            "success": True,
            "expression": str(expr),
            "series": str(series_result),
            "order": n
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
```

Puis ajoutez la commande dans `main.py`:

```python
if user_input.lower().startswith("taylor "):
    expr = user_input.split(" ", 1)[1]
    result = calculator.taylor_series(expr)
    # ... afficher le résultat
```

---

## 🔌 Intégrer une API externe

### Exemple: Intégrer une API de traduction

Créez `jarvis/agents/translator.py`:

```python
"""Agent pour la traduction"""
import requests
from typing import Dict

class Translator:
    """Traduit du texte"""
    
    def translate(self, text: str, source: str = "fr", target: str = "en") -> Dict[str, str]:
        """Traduit du texte via une API gratuite"""
        try:
            url = f"https://api.mymemory.translated.net/get"
            params = {
                "q": text,
                "langpair": f"{source}|{target}"
            }
            
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            
            return {
                "success": True,
                "original": text,
                "translated": data["responseData"]["translatedText"],
                "from": source,
                "to": target
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
```

---

## 🎨 Personnaliser l'interface

Modifiez les chaînes dans `main.py`:

```python
# Personnalisez les messages
print_help()  # Dans cette fonction

# Ou créez une fonction personnalisée
def print_custom_help():
    help_text = """
    Vos commandes personnalisées ici
    """
    print(help_text)
```

---

## 🧪 Tester votre code

Créez `test_agents.py`:

```python
"""Tests pour les agents"""
from jarvis.agents import Calculator, ApplicationLauncher

def test_calculator():
    calc = Calculator()
    
    # Test dérivée
    result = calc.derivative("x**2 + 3*x")
    assert result["success"]
    assert "2*x + 3" in result["simplified"]
    print("✓ Test dérivée réussi")
    
    # Test équation
    result = calc.solve_equation("x**2 - 4")
    assert result["success"]
    assert len(result["solutions"]) > 0
    print("✓ Test équation réussi")

def test_app_launcher():
    launcher = ApplicationLauncher()
    
    # Test liste d'apps
    apps = launcher.list_installed_apps()
    assert len(apps) > 0
    print(f"✓ {len(apps)} applications disponibles")

if __name__ == "__main__":
    test_calculator()
    test_app_launcher()
    print("\n✓ Tous les tests réussis!")
```

Lancez les tests:
```bash
C:/Users/benja/AppData/Local/Python/pythoncore-3.14-64/python.exe test_agents.py
```

---

## 📊 Logging et débogage

Ajoutez du logging dans `jarvis/utils/logger.py`:

```python
"""Logging pour Jarvis"""
import logging
import os

def get_logger(name: str) -> logging.Logger:
    """Crée un logger"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Fichier de log
    handler = logging.FileHandler("jarvis.log")
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger
```

Utilisez-le dans vos agents:

```python
from jarvis.utils.logger import get_logger

logger = get_logger(__name__)

def some_function():
    logger.debug("Message de debug")
    logger.error("Message d'erreur")
```

---

## 🚀 Déployer votre extension

### 1. Créer un dossier pour votre extension
```
jarvis/extensions/
└── my_weather_plugin/
    ├── __init__.py
    ├── weather.py
    └── config.py
```

### 2. Charger les extensions automatiquement

Créez `jarvis/extension_loader.py`:

```python
"""Charge les extensions Jarvis"""
import os
import importlib

def load_extensions():
    """Charge tous les modules d'extension"""
    extensions = {}
    ext_dir = os.path.join(os.path.dirname(__file__), "extensions")
    
    for ext_name in os.listdir(ext_dir):
        ext_path = os.path.join(ext_dir, ext_name)
        if os.path.isdir(ext_path):
            try:
                module = importlib.import_module(f"jarvis.extensions.{ext_name}")
                extensions[ext_name] = module
                print(f"✓ Extension chargée: {ext_name}")
            except Exception as e:
                print(f"✗ Erreur chargement {ext_name}: {e}")
    
    return extensions
```

---

## 📚 Ressources pour développeurs

### Documentation Ollama API
```
GET http://localhost:11434/api/tags
POST http://localhost:11434/api/generate
POST http://localhost:11434/api/chat
```

### Bibliothèques recommandées
- `requests` - HTTP requests
- `sympy` - Calculs symboliques
- `numpy` - Calculs numériques
- `pandas` - Données
- `matplotlib` - Graphiques

### Installer plus de dépendances
```bash
C:/Users/benja/AppData/Local/Python/pythoncore-3.14-64/python.exe -m pip install numpy pandas matplotlib
```

---

## 🎯 Bonnes pratiques

1. **Structure modulaire** - Chaque agent dans son fichier
2. **Gestion des erreurs** - Toujours retourner `{"success": False, "error": ...}`
3. **Documentation** - Commentaires clairs et docstrings
4. **Tests** - Testez vos fonctions
5. **Performance** - Utilisez du caching si nécessaire
6. **Sécurité** - Validez les entrées utilisateur

---

## 🆘 Besoin d'aide?

1. Vérifiez les logs: `jarvis.log`
2. Testez votre code avec Python directement
3. Vérifiez que Ollama fonctionne: `ollama ps`
4. Consultez la documentation officielle

---

**Bon développement! 🚀**
