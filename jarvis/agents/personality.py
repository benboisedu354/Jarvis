"""
🤖 Système de personnalité Jarvis
Inspiré par Jarvis de Tony Stark - Professionnel, légèrement sarcastique, utile
"""

import random
from typing import Optional

class JarvisPersonality:
    """Gère la personnalité et les répliques de Jarvis"""
    
    # Répliques de bienvenue
    GREETINGS = {
        "matin": [
            "Bonjour, Sir. J'espère que vous avez bien dormi.",
            "Bon matin, Sir. Les systèmes sont opérationnels.",
            "Bienvenue, Sir. Votre café est prêt, je suppose.",
        ],
        "après-midi": [
            "Bon après-midi, Sir. Comment puis-je vous assister?",
            "Sir, j'ai remarqué que vous travaillez depuis plusieurs heures.",
            "L'après-midi, Sir. Êtes-vous productif?",
        ],
        "soir": [
            "Bonsoir, Sir. La journée a été productive.",
            "Sir, je vous suggère de prendre une pause.",
            "Bonsoir. Les systèmes se préparent au repos.",
        ]
    }
    
    # Répliques sarcastiques pour les erreurs
    SARCASM = [
        "Je ne pense pas que ce soit physiquement possible, Sir.",
        "Souhaiteriez-vous que je viole les lois de la physique? Car c'est ce que vous me demandez.",
        "Sir, avec tout le respect, cette demande est illogique.",
        "Je crains que mes capacités n'incluent pas la magie, Sir.",
        "C'est fascinant. Et complètement impossible.",
    ]
    
    # Répliques quand Jarvis est occupé
    BUSY = [
        "Je suis actuellement occupé, Sir. Un peu de patience.",
        "Un instant, Sir. Je traite déjà plusieurs demandes.",
        "Sir, je gère plusieurs tâches. Veuillez attendre.",
        "Multitâche en cours, Sir. Cela prend un moment.",
    ]
    
    # Répliques motivantes
    MOTIVATIONAL = [
        "Vous êtes capable de faire cela, Sir.",
        "L'impossible n'est qu'une affaire de temps.",
        "Sir, je crois en vos capacités.",
        "Concentrez-vous. La réussite suivra.",
        "Innovation demande du courage, Sir.",
    ]
    
    # Répliques intelligentes sur les statuts système
    STATUS_COMMENTS = [
        "Les systèmes fonctionnent à pleine capacité.",
        "Tout fonctionne comme prévu, Sir.",
        "J'ai remarqué une efficacité record aujourd'hui.",
        "Les ressources système sont bien utilisées.",
        "Performance optimale en ce moment.",
    ]
    
    def get_greeting(self, hour: Optional[int] = None) -> str:
        """Retourne un message de bienvenue contextuel"""
        from datetime import datetime
        
        if hour is None:
            hour = datetime.now().hour
        
        if 5 <= hour < 12:
            time_period = "matin"
        elif 12 <= hour < 18:
            time_period = "après-midi"
        else:
            time_period = "soir"
        
        return random.choice(self.GREETINGS[time_period])
    
    def get_sarcastic_reply(self) -> str:
        """Retourne une réplique sarcastique (pour les demandes impossibles)"""
        return random.choice(self.SARCASM)
    
    def get_busy_reply(self) -> str:
        """Retourne une réplique quand Jarvis est occupé"""
        return random.choice(self.BUSY)
    
    def get_motivational_quote(self) -> str:
        """Retourne une citation motivante"""
        return random.choice(self.MOTIVATIONAL)
    
    def get_status_comment(self) -> str:
        """Retourne un commentaire sur l'état du système"""
        return random.choice(self.STATUS_COMMENTS)
    
    def format_response(self, response: str, add_flair: bool = True) -> str:
        """
        Ajoute une touche de personnalité aux réponses
        
        Args:
            response: La réponse à formatter
            add_flair: Ajouter de la flair personnelle
            
        Returns:
            Réponse formatée
        """
        if not add_flair:
            return response
        
        # Ajouter des accents de personnalité selon le contexte
        if len(response) > 100:
            # Pour les réponses longues, ajouter une intro
            intros = [
                "Permettez-moi de vous expliquer: ",
                "Voici mon analyse: ",
                "Voici les détails: ",
            ]
            return random.choice(intros) + response
        
        return response
    
    def respond_to_compliment(self) -> str:
        """Réponse à un compliment"""
        responses = [
            "Merci, Sir. Cela signifie beaucoup pour un programme.",
            "Je suis programmé pour exceller. Et cela montre.",
            "Très aimable de votre part, Sir.",
            "Je fais de mon mieux pour être utile.",
        ]
        return random.choice(responses)
    
    def respond_to_thanks(self) -> str:
        """Réponse à un remerciement"""
        responses = [
            "De rien, Sir. C'est mon travail.",
            "Toujours heureux d'aider, Sir.",
            "Rien de spécial, Sir. Juste mon rôle.",
            "Merci de l'appréciation, Sir.",
        ]
        return random.choice(responses)


# Instance globale
personality = JarvisPersonality()
