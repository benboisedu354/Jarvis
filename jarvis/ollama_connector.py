"""Connecteur pour Ollama"""
import requests
import json
from typing import Optional
from .config import OLLAMA_HOST, OLLAMA_MODEL

class OllamaConnector:
    def __init__(self, host: str = OLLAMA_HOST, model: str = OLLAMA_MODEL):
        self.host = host
        self.model = model
        self.generate_url = f"{host}/api/generate"
        self.chat_url = f"{host}/api/chat"
        
    def check_connection(self) -> bool:
        """Vérifie si Ollama est accessible"""
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def get_available_models(self) -> list:
        """Récupère la liste des modèles disponibles"""
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=5)
            data = response.json()
            return [model["name"] for model in data.get("models", [])]
        except Exception as e:
            print(f"Erreur lors de la récupération des modèles: {e}")
            return []
    
    def generate_response(self, prompt: str, stream: bool = False) -> str:
        """Génère une réponse via Ollama"""
        try:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": stream
            }
            
            response = requests.post(
                self.generate_url, 
                json=payload, 
                timeout=30
            )
            
            if stream:
                full_response = ""
                for line in response.iter_lines():
                    if line:
                        chunk = json.loads(line)
                        full_response += chunk.get("response", "")
                return full_response.strip()
            else:
                data = response.json()
                return data.get("response", "").strip()
                
        except Exception as e:
            print(f"Erreur lors de la génération: {e}")
            return f"Erreur: {e}"
    
    def chat(self, messages: list, stream: bool = False) -> str:
        """Mode chat avec historique"""
        try:
            payload = {
                "model": self.model,
                "messages": messages,
                "stream": stream
            }
            
            response = requests.post(
                self.chat_url,
                json=payload,
                timeout=30
            )
            
            if stream:
                full_response = ""
                for line in response.iter_lines():
                    if line:
                        chunk = json.loads(line)
                        full_response += chunk.get("message", {}).get("content", "")
                return full_response.strip()
            else:
                data = response.json()
                return data.get("message", {}).get("content", "").strip()
                
        except Exception as e:
            print(f"Erreur lors du chat: {e}")
            return f"Erreur: {e}"
