# InvexTrack

InvexTrack est une plateforme innovante de gestion des objectifs et des tâches, conçue pour aider les individus et les équipes à planifier, suivre et atteindre leurs objectifs efficacement. Ce projet s'inscrit dans la suite d'outils InvexManager, dédiée à la transformation numérique et à l'optimisation des processus.

## Fonctionnalités principales

- **Suivi des objectifs** : Créez, planifiez et suivez vos objectifs personnels et professionnels.
- **Gestion des tâches** : Organisez vos tâches avec des priorités, des échéances et des rappels.
- **Tableaux de bord personnalisés** : Visualisez vos progrès en temps réel grâce à des graphiques interactifs.
- **Collaboration en équipe** : Partagez des objectifs et des tâches, et travaillez en temps réel avec vos collègues.
- **Avatar interactif** : Interagissez avec *Léora*, l’assistante virtuelle qui vous guide et vous motive.
- **Intégrations** : Connectez InvexTrack à d'autres outils de productivité et de gestion.

## Technologies utilisées

- **Backend** : Python (Django)
- **Frontend** : React.js
- **Base de données** : PostgreSQL
- **Infrastructure** : Docker, AWS (ou autre solution d’hébergement)
- **Tests** : Pytest, Jest
- **Outils CI/CD** : GitHub Actions, Docker Compose

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/invextrack.git
   cd invextrack
   ```

2. Configurez l’environnement virtuel Python :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Installez les dépendances frontend :
   ```bash
   cd frontend
   npm install
   ```

4. Configurez les variables d’environnement en créant un fichier `.env` basé sur `.env.example`.

5. Lancez l’application :
   ```bash
   docker-compose up --build
   ```

6. Accédez à l’application à l’adresse suivante :
   ```
   http://localhost:8000
   ```

## Contribution

Nous accueillons volontiers les contributions pour améliorer InvexTrack. Voici comment vous pouvez contribuer :

1. Forkez le dépôt.
2. Créez une branche pour votre fonctionnalité ou correctif :
   ```bash
   git checkout -b ma-nouvelle-fonctionnalite
   ```
3. Faites vos modifications et ajoutez-les à l’index :
   ```bash
   git add .
   ```
4. Faites un commit avec un message descriptif :
   ```bash
   git commit -m "Ajout d'une nouvelle fonctionnalité"
   ```
5. Poussez vos modifications vers votre fork :
   ```bash
   git push origin ma-nouvelle-fonctionnalite
   ```
6. Ouvrez une Pull Request vers la branche principale.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.

## Contact

Pour toute question ou suggestion, contactez-nous à :  
📧 **infos@invexcam.com**

---

*InvexTrack - Simplifiez votre gestion, maximisez vos résultats !*
