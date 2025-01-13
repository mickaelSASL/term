# Consultation d'une BDD en Python

## Module à installer
```Python
pip install mysql.connector
```

## Exemple d'interogation d'une base de données en Python

```Python
import mysql.connector
from mysql.connector import errorcode

# Caractéristiques de la connection
database    = 'villes'
host_ip     = 'localhost'
utilisateur = 'moi'
password    = ''

#####################
# CONNECTION à la BDD
#####################
try:   
  conn = mysql.connector.connect(
      user = utilisateur, 
      password = password,
      host = host_ip,
      database = database)

#################################
# la connection à la BDD a échoué   
#################################
except mysql.connector.Error as err:    
    
    # Si Erreur de nom d'utilisateur ou de mot de passe
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Votre nom d'utilisateur ou votre mot de passe ne correspond pas !")
    
    # Si Erreur de nom de base de données
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de données",database,"n'existe pas")
    # Si autre Erreur
    else:
        print(err)

#################################
# La connection à la BDD a réussi 
#################################
else:         
    print("vous êtes connecté à la base", conn._database)

##################################################################  
# On créé un curseur MySQL qui contient le résultat de la requête
##################################################################
    curseur = conn.cursor(buffered=True)
    
###################################
# REQUETE SQL : Sélection méthode 1
###################################
    requete=("SELECT ville_nom, ville_code_postal FROM villes_france_free;")  # Requête SQL
    resultat = curseur.execute(requete)           # Execution de la requete
    
    # On lit toutes les lignes de 'resultat' pour les affecter à 'table'
    table = curseur.fetchall()
    print(table)     # résultat : liste de tuples

    # Après la lecture des entrées du résultat de la requête avec
    # 'curseur.fetchall()', 'curseur' est vidé.
    
    print()    
###################################
# REQUETE SQL : Sélection méthode 2
###################################
    requete=("SELECT ville_nom, ville_code_postal FROM villes_france_free WHERE ville_nom='Auray';")
    resultat = curseur.execute(requete)
    

    for (nom_de_ville, le_cp) in curseur:
        print("nom :", nom_de_ville, "/ code postal :", le_cp)
    
    # le tuple de la boucle for (ici '(nnom_de_ville, le_cp)') doit contenir autant d'éléments
    # que d'éléments dans la requête ('ville_nom, ville_code_postal')

#######################################
# REQUETE SQL : Modification de données
#######################################
    requete=("UPDATE villes_france_free SET ville_population_2012='"+ input("Nouveau Population :")+"' WHERE ville_nom='Auray';")
    resultat = curseur.execute(requete)
    
    conn.commit()  # Les modifications sont appliquées dans la BDD
    
    # 'commit()' est nécessaire pour les requêtes de modification
    

    curseur.close()  # fermeture du curseur
    conn.close()     # fermeture du connection
```


## Exercice


!!! Question "1. Recopier le code ci-dessus et le tester (pensez à modifier les informations de connexion au serveur)"


!!! Question "2. Ecrire un requête permettant de récupérer le nombre de villes par département."
    pour cela il faut utiliser SELECT, JOIN, COUNT, GROUP BY

    résultat attendu :
    ``` python
    [(419, 'Ain'), (1176, 'Aisne'), (320, 'Allier'), (200, 'Alpes-de-Haute-Provence'), (163, 'Alpes-Maritimes'), (339, 'Ardèche'), (463, 'Ardennes'), (332, 'Ariège'), (433, 'Aube'), (438, 'Aude'), (304, 'Aveyron'), (377, 'Bas-Rhin'), (119, 'Bouches-du-Rhône'), (706, 'Calvados'), (260, 'Cantal'), (404, 'Charente'), (472, 'Charente-Maritime'), (290, 'Cher'), (286, 'Corrèze'), (373, "Côte-d'or"), (260, "Côtes-d'armor"), (557, 'Creuse'), (782, 'Deux-Sèvres'), (594, 'Dordogne'), (369, 'Doubs'), (675, 'Drôme'), (36, 'Essonne'), (403, 'Eure'), (283, 'Eure-et-Loir'), (353, 'Finistère'), (589, 'Gard'), (542, 'Gers'), (343, 'Gironde'), (293, 'Haut-Rhin'), (706, 'Haute-corse'), (463, 'Haute-Garonne'), (221, 'Haute-Loire'), (261, 'Haute-Marne'), (573, 'Haute-Saône'), (1, 'Haute-Savoie'), (515, 'Haute-Vienne'), (177, 'Hautes-Alpes'), (226, 'Hautes-Pyrénées'), (40, 'Hauts-de-Seine'), (353, 'Hérault'), (247, 'Ile-et-Vilaine'), (277, 'Indre'), (533, 'Indre-et-Loire'), (544, 'Isère'), (331, 'Jura'), (291, 'Landes'), (327, 'Loir-et-Cher'), (260, 'Loire'), (334, 'Loire-Atlantique'), (340, 'Loiret'), (319, 'Lot'), (185, 'Lot-et-Garonne'), (363, 'Lozère'), (601, 'Maine-et-Loire'), (620, 'Manche'), (433, 'Marne'), (594, 'Mayenne'), (500, 'Meurthe-et-Moselle'), (261, 'Meuse'), (730, 'Morbihan'), (312, 'Moselle'), (650, 'Nièvre'), (693, 'Nord'), (505, 'Oise'), (895, 'Orne'), (745, 'Paris'), (470, 'Pas-de-Calais'), (547, 'Puy-de-Dôme'), (474, 'Pyrénées-Atlantiques'), (527, 'Pyrénées-Orientales'), (545, 'Rhône'), (375, 'Saône-et-Loire'), (305, 'Sarthe'), (294, 'Savoie'), (262, 'Seine-et-Marne'), (514, 'Seine-Maritime'), (47, 'Seine-Saint-Denis'), (323, 'Somme'), (195, 'Tarn'), (153, 'Tarn-et-Garonne'), (196, 'Territoire de Belfort'), (185, 'Val-de-Marne'), (151, 'Var'), (282, 'Vaucluse'), (281, 'Vendée'), (201, 'Vienne'), (455, 'Vosges'), (102, 'Yonne'), (305, 'Yvelines')]
    ```
    ??? note "Solution"

        ```SQL
        SELECT count(*), departement_nom 
        FROM villes_france_free JOIN departement 
        ON villes_france_free.ville_departement = departement.departement_id 
        GROUP BY departement_nom
        ```
!!! Question "3. Exploiter ces données pour construire un diagramme circulaire présentant la répartition des communes par département."
    Utiliser la bibliothèque [*'matplotlib'*](https://matplotlib.org/)

    résultat attendu :

    ![](Figure.png)