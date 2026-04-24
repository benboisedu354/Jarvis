# 🚀 JARVIS - Démarrage Rapide

## ✅ Configuration complète!

Votre Jarvis est prêt à être utilisé. Voici comment commencer:

---

## 📍 ÉTAPE 1: Démarrer Ollama

**Ouvrez un terminal PowerShell/CMD et exécutez:**
```bash
ollama serve
```

Laissez ce terminal ouvert (c'est le serveur Ollama).

---

## 📍 ÉTAPE 2: Télécharger un modèle léger

**Ouvrez un AUTRE terminal et exécutez:**
```bash
# Mistral 7B (Recommandé - 4-5GB)
ollama pull mistral

# OU une alternative plus légère:
ollama pull neural-chat
ollama pull dolphin-phi
ollama pull orca-mini
```

Attendez que le modèle soit téléchargé (quelques minutes).

---

## 📍 ÉTAPE 3: Lancer Jarvis

**Double-cliquez sur `jarvis.bat`**

Ou en ligne de commande:
```bash
cd c:\Users\benja\Documents\Dev\Jarvis
C:/Users/benja/AppData/Local/Python/pythoncore-3.14-64/python.exe main.py
```

---

## 🎯 Exemples de commandes

```
Ouvrir une application:
  💬 ouvre notepad
  💬 ouvre chrome
  💬 lance calculatrice

Calculs mathématiques:
  💬 dérivée x**2 + 3*x
  💬 intégrale x**3
  💬 résous x**2 - 4 = 0
  💬 calcule sqrt(144)

Tâches basiques:
  💬 heure
  💬 date
  💬 recherche meteo marseille
  
Questions générales:
  💬 Pourquoi le ciel est bleu?
  💬 Explique moi la théorie de la relativité
  💬 Quel est la capital de la France?

Commandes système:
  💬 aide        → Affiche l'aide complète
  💬 quit        → Quitter
```

---

## ⚡ IMPORTANT - Problèmes courants

### ❌ "Impossible de se connecter à Ollama"
```
✓ Solution: Vérifiez qu'Ollama est lancé (ollama serve)
```

### ❌ "Model not found"
```
✓ Solution: Téléchargez le modèle: ollama pull mistral
```

### ❌ "Out of Memory"
```
✓ Solution: Utilisez un modèle plus léger
  ollama pull orca-mini
  
✓ Puis éditez .env:
  OLLAMA_MODEL=orca-mini:latest
```

### ❌ "Python command not found"
```
✓ Solution: Utilisez le chemin complet:
  C:/Users/benja/AppData/Local/Python/pythoncore-3.14-64/python.exe main.py
```

---

## 📊 Modèles par taille VRAM

```
RTX 3070 8GB → mistral:latest (Recommandé)
RTX 3070 6GB → neural-chat OU dolphin-phi
RTX 3070 4GB → orca-mini
```

---

## 💾 Configuration (.env)

Fichier: `c:\Users\benja\Documents\Dev\Jarvis\.env`

```env
OLLAMA_HOST=http://localhost:11434    # Ne changez pas
OLLAMA_MODEL=mistral:latest           # Changez le modèle si nécessaire
USE_TTS=False                          # Synthèse vocale (experimental)
```

---

## 🔍 Commandes Ollama utiles

```bash
# Voir les modèles téléchargés
ollama list

# Voir la consommation mémoire
ollama ps

# Télécharger un modèle
ollama pull mistral

# Supprimer un modèle pour libérer de la VRAM
ollama rm mistral
```

---

## 📚 Documentation complète

Voir `README.md` pour plus de détails.

---

**Prêt à utiliser Jarvis? 🚀**

Lancez `jarvis.bat` et commencez!

---

*Créé pour RTX 3070 8GB*
