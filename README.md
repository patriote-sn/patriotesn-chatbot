# patriotesn-chatbot

Une API REST construite avec FastAPI, permettant d'interroger un index Pinecone contenant des documents juridiques. Cette API utilise OpenAI pour répondre aux questions en s'appuyant sur un modèle conversationnel basé sur la récupération de documents.

## Fonctionnalités

- **Question/Réponse Juridique :** Posez des questions et recevez des réponses basées sur des documents indexés.
- **Support d'Index Pinecone :** L'API s'appuie sur un index Pinecone existant pour stocker et interroger les données.
- **LangChain :** Utilisation de LangChain pour orchestrer les interactions avec les modèles OpenAI et le système de récupération.

## Prérequis

Avant de lancer ce projet, assurez-vous d'avoir installé :

- **Python** (>= 3.8.1)
- Un environnement virtuel Python (optionnel mais recommandé)
- **Pip** à jour :
  ```bash
  python -m pip install --upgrade pip





