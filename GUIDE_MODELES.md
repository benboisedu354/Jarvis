# 📚 Guide complet des modèles Jarvis

## 🎯 Quelle RTX 3070 pour quel modèle?

### RTX 3070 8GB (Vous avez celle-ci!)

| Modèle | VRAM | Vitesse | Qualité | Recommandation |
|--------|------|---------|---------|-----------------|
| **Mistral 7B** | 4-5GB | ⚡⚡ Rapide | ⭐⭐⭐⭐⭐ Excellent | 🏆 **MEILLEUR CHOIX** |
| Neural Chat 7B | 3-4GB | ⚡⚡ Rapide | ⭐⭐⭐⭐ Très bon | ✅ Bon alternatif |
| Dolphin Phi 3B | 3GB | ⚡⚡⚡ Très rapide | ⭐⭐⭐ Bon | ✅ Pour plus de rapidité |
| Orca Mini 3B | 2GB | ⚡⚡⚡ Très rapide | ⭐⭐ Acceptable | ⚠️ Si manque de VRAM |

---

## 🚀 Installation des modèles

### Méthode 1: Installation automatique (Recommandée)
```bash
# Double-cliquez sur installer_modeles.bat
# Puis sélectionnez votre modèle
```

### Méthode 2: Ligne de commande
```bash
# Mistral (recommandé)
ollama pull mistral

# Alternatives
ollama pull neural-chat
ollama pull dolphin-phi
ollama pull orca-mini
```

---

## 🔧 Changer de modèle

### Option 1: Via le fichier `.env`
Éditez `c:\Users\benja\Documents\Dev\Jarvis\.env`:
```env
OLLAMA_MODEL=mistral:latest           # Changez ici
```

Modèles disponibles:
- `mistral:latest`
- `neural-chat:latest`
- `dolphin-phi:latest`
- `orca-mini:latest`

### Option 2: Vérifier les modèles installés
```bash
ollama list
```

---

## ✨ Capacités par modèle

### 🏆 Mistral 7B (RECOMMANDÉ)
```
✓ Excellente qualité de réponses
✓ Rapide et fluide
✓ Bon pour les calculs et explications
✓ Excellente compréhension du français
✓ Gestion mémoire optimale pour RTX 3070 8GB

Cas d'usage: Conversations générales, questions complexes, explications
```

### ✅ Neural Chat 7B
```
✓ Très bon pour les conversations
✓ Plus léger que Mistral
✓ Optimisé pour le chat
✓ Réponses plus courtes et directes

Cas d'usage: Discussions rapides, réponses concises
```

### ⚡ Dolphin Phi 3B
```
✓ Plus rapide que Mistral
✓ Moins de VRAM
✓ Capacités mathématiques réduites
✓ Bon pour les tâches simples

Cas d'usage: Questions basiques, tâches rapides
```

### 🔋 Orca Mini 3B
```
✓ Très léger (2GB)
✓ Très rapide
✓ Qualité réduite
✓ Basique mais fonctionnel

Cas d'usage: Tests, tâches très simples
```

---

## 📊 Performance et VRAM

### Surveillance de la consommation VRAM

```bash
# Voir les modèles chargés et leur consommation
ollama ps

# Exemple de sortie:
# NAME                    ID              SIZE      PROCESSOR % CPU % MEMORY
# mistral:latest          abc123def456    3.8 GB    100%      5.2   4.1 GB
```

### Si vous manquez de VRAM

```bash
# 1. Vérifiez la consommation
ollama ps

# 2. Arrêtez Ollama et redémarrez avec moins de modèles
# (les modèles se déchargent après inactivité)

# 3. Utilisez un modèle plus léger
# Editez .env:
OLLAMA_MODEL=orca-mini:latest
```

---

## 🎓 Tests de modèle

### Test 1: Qualité générale
```
Vous: Explique moi pourquoi le ciel est bleu?

Mistral ⭐⭐⭐⭐⭐: Explication détaillée sur la diffusion Rayleigh
Neural Chat ⭐⭐⭐⭐: Explication claire et concise
Dolphin Phi ⭐⭐⭐: Explication basique mais correcte
Orca Mini ⭐⭐: Réponse très simple
```

### Test 2: Calculs mathématiques
```
Vous: dérivée x**3 + 2*x**2 - 5*x + 1

Mistral ⭐⭐⭐⭐⭐: Réponse exacte: 3*x**2 + 4*x - 5
Neural Chat ⭐⭐⭐⭐: Réponse exacte
Dolphin Phi ⭐⭐⭐: Réponse correcte
Orca Mini ⭐⭐: Peut se tromper
```

### Test 3: Français
```
Vous: Accorde ce verbe: "Les enfants ont couru..."

Mistral ⭐⭐⭐⭐⭐: Explication complète
Neural Chat ⭐⭐⭐⭐: Bonne réponse
Dolphin Phi ⭐⭐⭐: Réponse basique
Orca Mini ⭐⭐: Peut se tromper
```

---

## 🔄 Changer rapidement de modèle

### Étape 1: Éditer `.env`
```bash
# Ouvrez: c:\Users\benja\Documents\Dev\Jarvis\.env
# Changez OLLAMA_MODEL

OLLAMA_MODEL=mistral:latest     # Par défaut
OLLAMA_MODEL=neural-chat:latest # Alternative 1
OLLAMA_MODEL=dolphin-phi:latest # Alternative 2
OLLAMA_MODEL=orca-mini:latest   # Alternative 3
```

### Étape 2: Relancer Jarvis
```bash
# Double-cliquez sur jarvis.bat
# ou
C:/Users/benja/AppData/Local/Python/pythoncore-3.14-64/python.exe main.py
```

---

## 💡 Recommandations

### Pour votre RTX 3070 8GB:

**🥇 Premier choix:** `mistral:latest`
- Meilleur équilibre qualité/vitesse
- 4-5GB VRAM
- Excellent pour tout

**🥈 Alternative:** `neural-chat:latest`
- Si vous préférez les réponses plus courtes
- 3-4GB VRAM
- Optimisé pour le chat

**🥉 Si problèmes de VRAM:** `dolphin-phi:latest`
- Plus léger
- Moins de qualité
- 3GB VRAM

---

## 🐛 Dépannage

### "CUDA out of memory"
```
✓ Solution:
1. Utilisez ollama ps pour voir la consommation
2. Changez de modèle (plus léger)
3. Attendez que le modèle se décharge (inactivité)
```

### "Model takes a long time to respond"
```
✓ Solution:
1. Vérifiez que vous n'avez pas d'autres programmes lourds
2. Vérifiez qu'Ollama n'est pas en train de télécharger
3. Essayez un modèle plus léger
```

### "Mauvaise qualité de réponses"
```
✓ Solution:
1. Vous utilisez un modèle trop léger
2. Changez pour Mistral (meilleure qualité)
3. Reformulez votre question plus clairement
```

---

## 📚 Ressources supplémentaires

- **Ollama**: https://ollama.ai
- **Mistral**: https://mistral.ai
- **Modèles**: https://ollama.ai/library

---

*Documentation pour Jarvis sur RTX 3070 8GB*
