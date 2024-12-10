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

git clone https://github.com/username/nom-du-repo.git
cd nom-du-repo

python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate

 
 pip install -r requirements.txt
OPENAI_API_KEY=your_openai_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENV=your_pinecone_environment_here


uvicorn main:app --reload
curl -X POST http://127.0.0.1:8000/ask \
-H "Content-Type: application/json" \
-d '{"question": "Quel est le droit applicable aux contrats au Sénégal ?"}'
{
  "answer": "Voici la réponse à votre question..."
}

.
├── main.py              # Fichier principal contenant l'API FastAPI
├── requirements.txt     # Liste des dépendances Python
├── .env                 # Fichier des variables d'environnement (non inclus dans le dépôt)
├── .gitignore           # Fichiers et dossiers ignorés par Git
└── README.md            # Documentation du projet

Variables d'Environnement
OPENAI_API_KEY : Clé API OpenAI
PINECONE_API_KEY : Clé API Pinecone
PINECONE_ENV : Environnement Pinecone (ex: us-west1-gcp)
Ne poussez jamais votre fichier .env sur le dépôt. Partagez-le de manière sécurisée avec votre équipe et utilisez un fichier env.example comme guide.

Déploiement
Pour un déploiement en production :

Configurer un serveur ou service cloud (AWS, Azure, Heroku, etc.).
Installer les dépendances sur le serveur.
Définir les variables d'environnement sur le serveur.
Lancer l'API :
bash
Copier le code
uvicorn main:app --host 0.0.0.0 --port 800



