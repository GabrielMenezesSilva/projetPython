# Documentation du Projet

## Structure du Projet

### Répertoire `.vscode`
- **`settings.json`** : Fichier de configuration pour Visual Studio Code du projet.

### Répertoire `app`
- **`__init__.py`** : Fichier d'initialisation du package `app`.
- **`app.py`** : Fichier principal de l'application Flask. Il configure et lance le serveur, enregistre les blueprints, et définit les routes principales.
- **`config/`** : Répertoire de configuration.
  - **`__init__.py`** : Fichier d'initialisation du package `config`.
  - **`mango_db.py`** : Fichier de configuration et d'interaction avec la base de données MongoDB.
- **`index.html`** : Page HTML principale de l'application.

### Répertoire `app/src`
#### Analyse
- **`analyse_controller.py`** : Contrôleur qui définit les routes liées à l'analyse.
- **`analyse_repository.py`** : Repository responsable de l'interaction avec les données d'analyse.
- **`analyse_service.py`** : Service qui contient la logique métier pour effectuer les analyses.
- **`analyse.py`** : Fichier principal pour la logique d'analyse.
- **`dto/`** : Répertoire pour les objets de transfert de données (DTO - Data Transfer Objects).
- **`test.ipynb`** : Notebook Jupyter pour les tests et expérimentations.

#### Cours
- **`cours_controller.py`** : Contrôleur qui définit les routes liées aux cours.
- **`cours_repository.py`** : Repository responsable de l'interaction avec les données des cours.
- **`cours_service.py`** : Service qui contient la logique métier pour gérer les cours.
- **`cours.py`** : Fichier principal pour la logique des cours.
- **`dto/`** : Répertoire pour les objets de transfert de données (DTO - Data Transfer Objects).

#### Professeurs
- **`prof_controller.py`** : Contrôleur qui définit les routes liées aux professeurs.
- **`prof_repository.py`** : Repository responsable de l'interaction avec les données des professeurs.
- **`prof_service.py`** : Service qui contient la logique métier pour gérer les professeurs.
- **`prof.py`** : Fichier principal pour la logique des professeurs.
- **`dto/`** : Répertoire pour les objets de transfert de données (DTO - Data Transfer Objects).

### Fichier `requirements.txt`
- Liste des dépendances et bibliothèques nécessaires au projet.

---

## Description des Fonctionnalités

### `app/app.py`
Ce fichier est le point d'entrée de l'application Flask. Il configure l'application, active le CORS, enregistre les blueprints des modules `cours` et `analyse`, et définit des routes principales comme `/ping` et `/api/submit`.

### `app/src/analyse/analyse_controller.py`
Définit les routes liées à l'analyse. Il utilise le service `AnalyseService` pour effectuer des opérations d'analyse et retourner les résultats sous forme de JSON.

### `app/src/analyse/analyse_service.py`
Contient la logique métier pour réaliser les analyses. Ce fichier inclut des méthodes pour calculer des analyses spécifiques, convertir des évaluations en DataFrames pandas, et formater les résultats en JSON.

### `app/src/analyse/analyse_repository.py`
Responsable de l'interaction avec les données d'analyse, telles que la récupération et l'enregistrement des informations dans la base de données.

### `app/src/cours/cours_controller.py`
Définit les routes liées aux cours. Utilise le service `CoursService` pour effectuer des opérations liées aux cours et retourner les résultats sous forme de JSON.

### `app/src/cours/cours_service.py`
Contient la logique métier pour gérer les cours. Il inclut des méthodes pour obtenir tous les cours et effectuer des opérations spécifiques sur les cours.

### `app/src/cours/cours_repository.py`
Responsable de l'interaction avec les données des cours, telles que la récupération et l'enregistrement des informations dans la base de données.

### `app/src/prof/prof_controller.py`
Définit les routes liées aux professeurs. Utilise le service `ProfService` pour effectuer des opérations liées aux professeurs et retourner les résultats sous forme de JSON.

### `app/src/prof/prof_service.py`
Contient la logique métier pour gérer les professeurs. Il inclut des méthodes pour effectuer des opérations spécifiques liées aux professeurs.

### `app/src/prof/prof_repository.py`
Responsable de l'interaction avec les données des professeurs, telles que la récupération et l'enregistrement des informations dans la base de données.

---

## Résumé du Projet

Cette documentation fournit un aperçu de la **structure du projet** ainsi que de la **fonctionnalité de chaque fichier**. Chaque fichier et chaque répertoire ont un rôle bien défini dans l'architecture de l'application, permettant une organisation modulaire et claire du code.

---
