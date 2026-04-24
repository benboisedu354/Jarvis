"""Configuration pour Jarvis"""
import os
from dotenv import load_dotenv

load_dotenv()

# Ollama Configuration
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral:latest")  # Modèle léger pour RTX 3070

# Models recommandés pour RTX 3070 8GB:
# - mistral:latest (7B) - 4-5GB
# - neural-chat (7B) - 3-4GB  
# - dolphin-phi (3B) - 3GB
# - orca-mini (3B) - 2GB

# Configuration TTS
USE_TTS = os.getenv("USE_TTS", "True").lower() == "true"
