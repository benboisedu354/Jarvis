# ✅ CHECKLIST - Avant de démarrer Jarvis

## 📋 Vérifications pré-lancement

### ✓ Système
- [ ] Windows 10/11
- [ ] RTX 3070 8GB (ou GPU équivalent)
- [ ] 16GB RAM minimum

### ✓ Logiciels installés
- [ ] Python 3.8+ installé
- [ ] Ollama téléchargé et installé

### ✓ Python configuré
- [ ] Python reconnu via: `C:/Users/benja/AppData/Local/Python/pythoncore-3.14-64/python.exe --version`
- [ ] pip fonctionne

### ✓ Dépendances installées
- [ ] requests ✓
- [ ] sympy ✓
- [ ] pyttsx3 ✓
- [ ] python-dotenv ✓

### ✓ Fichiers de configuration
- [ ] .env créé et configuré
- [ ] OLLAMA_HOST = http://localhost:11434
- [ ] OLLAMA_MODEL = mistral:latest

---

## 🚀 Étapes de démarrage (À faire une seule fois)

### Semaine 1: Installation

#### Lundi - Installation Ollama
```bash
# Téléchargez depuis: https://ollama.ai/download
# Installez Ollama
# Lancez: ollama serve
```
- [ ] Ollama installé
- [ ] Ollama se lance sans erreurs

#### Mardi - Télécharger un modèle
```bash
# Dans un autre terminal:
ollama pull mistral
# Attendez 10-20 minutes
```
- [ ] Mistral téléchargé
- [ ] Taille: ~4.1GB
- [ ] Modèle visible dans: ollama list

#### Mercredi - Tester Jarvis
```bash
# Double-cliquez jarvis.bat
# Testez quelques commandes
```
- [ ] Jarvis démarre
- [ ] Connexion Ollama OK
- [ ] Première réponse reçue
- [ ] Calculs mathématiques fonctionnent

---

## 📝 Utilisations quotidiennes

### Matin - Configuration
```
1. Ouvrir Terminal 1
2. Lancer: ollama serve
3. Ouvrir Terminal 2 (optionnel pour monitoring)
4. Double-cliquez jarvis.bat
```
- [ ] Ollama lancé
- [ ] Jarvis démarré
- [ ] Prêt à utiliser

### Travail - Utilisation
```
Ouvrir applications: ouvre chrome
Calculs: dérivée x**2
Questions: Pourquoi le ciel est bleu?
```
- [ ] Chaque commande reçoit une réponse
- [ ] Les réponses sont correctes
- [ ] Pas de lag significatif

### Soir - Fermeture
```
1. Fermer Terminal 1 (ollama serve)
   ou appuyez sur Ctrl+C
2. Fermer Terminal 2 (Jarvis)
   ou tapez: quit
```
- [ ] Ollama arrêté proprement
- [ ] Jarvis fermé
- [ ] Pas de processus résiduels

---

## 🐛 Vérifications si problèmes

### Ollama ne répond pas
```bash
# Vérifiez:
ollama ps                    # Voit les modèles chargés
ollama list                  # Liste les modèles
```
- [ ] Ollama tourne bien
- [ ] Port 11434 accessible
- [ ] Modèle chargé en mémoire

### Jarvis démarre mais pas de réponses
```bash
# Testez la connexion:
curl http://localhost:11434/api/tags
```
- [ ] Ollama répond sur localhost:11434
- [ ] Modèle dans la liste
- [ ] VRAM suffisante

### Erreurs de VRAM
```bash
# Vérifiez:
ollama ps     # Voir la consommation
nvidia-smi    # Voir la VRAM GPU
```
- [ ] VRAM disponible > 4GB
- [ ] Pas d'autres programmes lourds
- [ ] Modèle <= 5GB

### Python ne fonctionne pas
```bash
# Vérifiez le chemin:
C:/Users/benja/AppData/Local/Python/pythoncore-3.14-64/python.exe --version
```
- [ ] Version Python correcte
- [ ] Chemin correct dans jarvis.bat
- [ ] Path Windows modifié si nécessaire

---

## 💡 Performance - Ce qui ralentit Jarvis

### Mauvaise performance?
- [ ] Vérifiez que Ollama n'est pas occupé: `ollama ps`
- [ ] Cherchez d'autres processus lourds: Win+Maj+Esc
- [ ] Redémarrez Ollama si > 5 min inactif
- [ ] Utilisez un modèle plus léger si nécessaire

### Très mauvaise qualité de réponses?
- [ ] Vérifiez le modèle: `ollama list`
- [ ] Si orca-mini, changez pour mistral
- [ ] Reformulez votre question plus clairement
- [ ] Vérifiez que vous utilisez bien le bon modèle dans .env

---

## 📊 Monitoring - Commandes utiles

### Vérifier Ollama
```bash
ollama ps              # Modèles chargés + VRAM
ollama list            # Tous les modèles installés
ollama pull mistral    # Télécharger un modèle
ollama rm mistral      # Supprimer un modèle
```

### Vérifier GPU
```bash
nvidia-smi             # État GPU NVIDIA
gpu-z.exe              # Monitor GPU (si installé)
```

### Vérifier Python
```bash
python --version       # Si reconnu
pip list              # Packages installés
```

---

## 🎯 Optimisations recommandées

### Pour plus de vitesse
- [ ] Fermer navigateurs/programmes lourds
- [ ] Utiliser Mistral plutôt que Neural Chat
- [ ] Augmenter GPU Memory (dans Ollama settings si possible)

### Pour plus de qualité
- [ ] Utiliser Mistral au lieu d'Orca
- [ ] Augmenter le temps de réponse acceptable
- [ ] Formuler les questions clairement

### Pour économiser la VRAM
- [ ] Utiliser Orca-Mini
- [ ] Arrêter Ollama quand non utilisé
- [ ] Fermer autres programmes

---

## 🔄 Mise à jour des modèles

### Changer de modèle
1. [ ] Éditez .env
2. [ ] Changez OLLAMA_MODEL
3. [ ] Redémarrez Jarvis

### Télécharger un nouveau modèle
```bash
ollama pull neural-chat
# Puis changez .env:
OLLAMA_MODEL=neural-chat:latest
```

### Supprimer un modèle (libérer VRAM)
```bash
ollama rm mistral
```

---

## 📚 Documentation à consulter

Si besoin:
- [ ] DEMARRAGE_RAPIDE.md (début rapide)
- [ ] README.md (complet)
- [ ] GUIDE_MODELES.md (modèles)
- [ ] DEVELOPPEMENT.md (extensions)
- [ ] INSTALLATION_COMPLETE.txt (recap)

---

## ✨ Indicateurs que tout fonctionne

Vert ✓:
- [ ] Ollama se lance sans erreur
- [ ] Première réponse reçue en < 1min
- [ ] Calculs mathématiques corrects
- [ ] Applications s'ouvrent
- [ ] Pas de crash

Orange ⚠️:
- [ ] Réponses > 2 min (modèle pesant)
- [ ] Réponses de mauvaise qualité (modèle pas assez bon)
- [ ] GPU à 100% mais temps réponse OK

Rouge ✗:
- [ ] Erreur "Out of memory"
- [ ] Ollama ne se lance pas
- [ ] Jarvis ne démarre pas
- [ ] Python ne reconnu

---

## 📞 Besoin d'aide?

1. [ ] Vérifiez INSTALLATION_COMPLETE.txt
2. [ ] Consultez README.md
3. [ ] Lisez TROUBLESHOOTING dans DEMARRAGE_RAPIDE.md
4. [ ] Vérifiez les logs: jarvis.log (si créé)

---

## ✅ Résumé avant utilisation

- Ollama version: ___________
- Modèle principal: ___________
- VRAM disponible: ___________ GB
- Python version: ___________
- Date installation: ___________

**Status:** [ ] Prêt à utiliser

---

*Checklist pour Jarvis - Mis à jour 24/04/2026*
