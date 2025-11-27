# 🦁 Projet NSI – Gestion d’un Parc Animalier

## 🎯 Objectifs du projet

À travers ce projet, vous allez :

* Concevoir une base de données relationnelle complète
* Construire un schéma relationnel
* Créer une base MySQL avec des tables et des contraintes
* Insérer et manipuler des données via SQL
* Écrire un script Python connecté à MySQL
* Générer des statistiques et des graphiques Matplotlib
* Créer une mini-application Web affichant les données et les graphiques

## 🧩 1. Modélisation de la base

### Travail demandé

1. Proposer un **schéma relationnel**
2. Traduire ce schéma relationnel en **instructions SQL** (CREATE TABLE)

### Entités minimales à modéliser
* Animal (id, nom, espèce, sexe, date_naissance, poids, enclos_id…)
* Espèce (id, nom, famille, régime alimentaire)
* Enclos (id, nom, superficie, biome)
* Nourrissage (id, animal_id, date, type_nourriture, quantite)
* Intervention vétérinaire (id, animal_id, date, motif, compte_rendu)
________________________________________

## 🗄️ 2. Base MySQL

### Travail demandé

Vous créerez :

1. les **tables** avec clés primaires et étrangères 
2. un **jeu de données** cohérent (ou import depuis CSV fourni)
3. un **fichier .sql** comprenant les requêtes demandées

### Requêtes obligatoires
* Liste des animaux d’un enclos donné
* Répartition des animaux par espèce
* Dernier nourrissage de chaque animal
* Animaux avec intervention vétérinaire ce mois-ci
* Poids moyen par espèce
* Animaux les plus nourris
* Densité des enclos (nombre d’animaux / superficie)
________________________________________

## 🐍 3. Script Python

### Travail demandé

Vous développerez un **script Python** qui :

1. Se connecte à MySQL (avec `mysql.connector`)
2. Permet :

* d’ajouter un animal,
* d’enregistrer un nourrissage,
* d’enregistrer une intervention,
* d’exécuter les requêtes SQL,
* de générer des statistiques.

3. Génère des **graphiques** (avec `Matplotlib`)
Les graphiques devront être enregistrés en fichier PNG (ex : `static/stats/especes.png`).

### Graphiques obligatoires
1.	Histogramme du nombre d’animaux par espèce
2.	Courbe de la quantité totale de nourriture consommée par jour
3.	Diagramme en barres du nombre d’interventions vétérinaires par mois
________________________________________

## 🌐 4. Mini-site Web

Vous créerez une petite **application Web** permettant :

1. Pages données :
* Liste des animaux (avec filtre : espèce ou enclos)
* Fiche détaillée d'un animal
* Liste des interventions
* Liste des nourrissages

2. Pages statistiques pour :
* les chiffres clés (nombre d’animaux, espèces…)
* les graphiques Matplotlib générés par Python

3. Intégration des graphiques Matplotlib
Les images seront générées par Python puis affichées dans la page HTML via :
    ``` html
        <img src="/static/stats/especes.png" alt="Répartition par espèce">
    ```

4. Structure de base conseillée

    ```
    ├── app.py
    ├── templates
        ├── index.html
        ├── animaux.html
        ├── stats.html
    ├── static
        ├── css
        ├── stats
            ├── another.js
            ├── nourriture.png
            └── interventions.png
    ```

________________________________________

## 📝 5. Rendu attendu

* schéma relationnel
* Scripts SQL de création des tables
* Fichier de données (INSERT ou CSV)
* Script Python complet
* Graphiques Matplotlib enregistrés et intégrés dans les pages
* Mini-site Web fonctionnel
* README expliquant le fonctionnement de l’application
 

## 🐾 6. Fichiers CSV

!!! Abstract "📄 especes.csv <a href='CSV\especes.csv'><img src='\term/images/download.png'></a>"
    ```csv-path
        id,nom,famille,regime_alimentaire
        1,Lion,Félin,Carnivore
        2,Zèbre,Équidés,Herbivore
        3,Perroquet,Psittacidés,Omnivore
        4,Pingouin,Sphéniscidés,Piscivore
        5,Tortue,Cheloniidae,Herbivore
    ```
________________________________________
!!! Abstract "📄 enclos.csv <a href='CSV\enclos.csv'><img src='\term/images/download.png'></a>"
    ``` csv
        id,nom,superficie,biome
        1,Savane,2500,Savane africaine
        2,Marais,1800,Zone humide
        3,Volière,600,Tropical
        4,Glacier,2000,Climat froid
    ```
________________________________________
!!! Abstract "📄 animaux.csv <a href='CSV\animaux.csv'><img src='\term/images/download.png'></a>"
    ``` csv
        id,nom,espece_id,sexe,date_naissance,poids,enclos_id
        1,Simba,1,M,2018-05-12,190,1
        2,Nala,1,F,2019-07-03,175,1
        3,Rayure,2,M,2020-03-22,320,1
        4,Bambou,5,F,2015-06-15,80,2
        5,Paco,3,M,2021-02-10,1.2,3
        6,Lola,3,F,2022-09-01,0.9,3
        7,Glagla,4,M,2017-11-30,35,4
        8,Frimas,4,F,2018-12-10,33,4
        9,Carapace,5,M,2010-04-05,95,2
        10,Galipette,3,F,2021-05-18,1.1,3
    ```
    
________________________________________
!!! Abstract "📄 nourrissages.csv <a href='CSV\nourrissages.csv'><img src='\term/images/download.png'></a>"
    ``` csv
        id,animal_id,date,type_nourriture,quantite
        1,1,2024-11-01,Viande rouge,6
        2,2,2024-11-01,Viande rouge,5
        3,3,2024-11-01,Foin,8
        4,5,2024-11-01,Graines,0.2
        5,6,2024-11-01,Graines,0.15
        6,7,2024-11-01,Poisson,1
        7,8,2024-11-01,Poisson,1.1
        8,4,2024-11-01,Légumes,1.5
        9,9,2024-11-01,Légumes,1.2
        10,1,2024-11-02,Viande rouge,6.3
        11,7,2024-11-02,Poisson,1
        12,5,2024-11-02,Graines,0.25
    ```
________________________________________
!!! Abstract "📄 interventions.csv <a href='CSV\interventions.csv'><img src='\term/images/download.png'></a>"
    ``` csv
        id,animal_id,date,motif,compte_rendu
        1,1,2024-10-10,Contrôle annuel,RAS
        2,2,2024-10-12,Blessure patte soignée,Antibiotiques 5 jours
        3,5,2024-09-20,Perte de plumes,Ajout vitamines
        4,7,2024-08-15,Problème respiration,Début traitement
        5,9,2024-07-01,Contrôle carapace,RAS
    ```
________________________________________