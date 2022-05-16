# **BDD4 - Langage SQL**

<center><img src="https://files.realpython.com/media/Build-a-Contact-Book_Watermarked.02531f28c45c.jpg" width="75%"></center>

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EaNYCjV5PN1KoKtEBdNzsZ4BxCGmC-oetJ_0PgZD9ZJBUQ?e=ppZReE
" target="_blank">Document de cours<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>

## Illustration des jointures

<a href="https://datascientest.com/tout-comprendre-des-jointures-sql">site à consulter</a>
<img style="bacground-color: #FFFFFF;" src="join.png">

## TD sur base distante

- Connecter vous sur la base de données `villes` située sur le serveur `192.168.2.107`, à l'aide de l'identifiant : `Prénom` et du mot de passe : `Nom`.
- Veuillez trouver les requêtes SQL permettant d’effectuer chacune des demandes suivantes :  

    1. Obtenir la liste des 10 villes les plus peuplées en 2012
    2. Obtenir la liste des 50 villes ayant la plus faible superficie
    3. Obtenir la liste des départements d’outres-mer, c’est-à-dire ceux dont le numéro de département commencent par “97”
    4. Obtenir le nom des 10 villes les plus peuplées en 2012, ainsi que le nom du département associé
    5. Obtenir la liste du nom de chaque département, associé à son code et du nombre de commune au sein de ces département, en triant afin d’obtenir en priorité les départements qui possèdent le plus de communes
    6. Obtenir la liste des 10 plus grands départements, en terme de superficie
    7. Compter le nombre de villes dont le nom commence par “Saint”
    8. Obtenir la liste des villes qui ont un nom existants plusieurs fois, et trier afin d’obtenir en premier celles dont le nom est le plus souvent utilisé par plusieurs communes
    9. Obtenir en une seule requête SQL la liste des villes dont la superficie est supérieur à la superficie moyenne
    10. Obtenir la liste des départements qui possèdent plus de 2 millions d’habitants
    11. Remplacez les tirets par un espace vide, pour toutes les villes commençant par “SAINT-” (dans la colonne qui contient les noms en majuscule)


### Aide

1. COUNT  
La fonction `COUNT()` permet de compter le nombre d’enregistrement dans une table.
```SQL
SELECT COUNT(*) FROM table
```
Il est aussi possible de connaitre le nombre d’enregistrement sur une colonne en particulier. Les enregistrements qui possèdent la valeur nul ne seront pas comptabilisé. La syntaxe pour compter les enregistrement sur la colonne “nom_colonne” est la suivante :
```SQL
SELECT COUNT(nom_colonne) FROM table
```

2. SUM  
La fonction `SUM()` permet de calculer la somme totale d’une colonne contenant des valeurs numériques.
```SQL
SELECT SUM(nom_colonne)
FROM table
```

3. AVG  
La fonction ``ÀVG()`` permet de calculer une valeur moyenne sur un ensemble d’enregistrement de type numérique et non nul.
```SQL
SELECT AVG(nom_colonne) FROM nom_table
```

4. LIKE  
L’opérateur `LIKE` est utilisé dans la clause `WHERE` des requêtes SQL. Ce mot-clé permet d’effectuer une recherche sur un modèle particulier. Il est par exemple possible de rechercher les enregistrements dont la valeur d’une colonne commence par telle ou telle lettre.
```SQL
SELECT *
FROM table
WHERE colonne LIKE modele
```
Dans cet exemple le “modèle” n’a pas été défini, mais il ressemble très généralement à l’un des exemples suivants:

    - `LIKE ‘%a’` : le caractère “%” est un caractère joker qui remplace tous les autres caractères. Ainsi, ce modèle permet de rechercher toutes les chaines de caractère qui se termine par un “a”.  
    - `LIKE ‘a%’` : ce modèle permet de rechercher toutes les lignes de “colonne” qui commence par un “a”.  
    - `LIKE ‘%a%’` : ce modèle est utilisé pour rechercher tous les enregistrement qui utilisent le caractère “a”.  
    - `LIKE ‘pa%on’` : ce modèle permet de rechercher les chaines qui commence par “pa” et qui se terminent par “on”, comme “pantalon” ou “pardon”.  
    - `LIKE ‘a_c’` : peu utilisé, le caractère “_” (underscore) peut être remplacé par n’importe quel caractère, mais un seul caractère uniquement (alors que le symbole pourcentage “%” peut être remplacé par un nombre incalculable de caractères . Ainsi, ce modèle permet de retourner les lignes “aac”, “abc” ou même “azc”.  

5. HAVING  
La condition `HAVING` est presque similaire à `WHERE` à la seule différence que `HAVING` permet de filtrer en utilisant des fonctions telles que `SUM()`, `COUNT()`, `AVG()`, `MIN()` ou `MAX()`.
```SQL
SELECT colonne1, SUM(colonne2)
FROM nom_table
GROUP BY colonne1
HAVING fonction(colonne2) operateur valeur
```

6. REPLACE
La fonction `REPLACE` permet de remplacer des caractères alphanumérique dans une chaîne de caractère. Cela sert particulièrement à mettre à jour des données dans une base de données ou à afficher des résultats personnalisés.
```SQL
SELECT REPLACE('Hello tout le monde', 'Hello', 'Bonjour');
```

7. GROUP BY

Clause de l’instruction `SELECT` qui scinde le résultat de la requête en groupes de lignes, généralement pour effectuer ensuite une ou plusieurs agrégations sur chaque groupe. L’instruction `SELECT` retourne une ligne par groupe.
```SQL
SELECT ColumnA, ColumnB FROM T GROUP BY ColumnA; 
```

Résultat :
```SQL
Bonjour tout le monde
```

> ### fichiers de la base de données :  
> * [table `departement.sql`](departement.sql)
> * [table `villes_france.sql`](villes_france.sql)


## Consultation d'une BDD en Python

### Module à installer
```Python
pip install mysql.connector
```

### Exemple d'interogation d'une base de données en Python

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
    requete=("UPDATE villes_france_free SET ville_population_2012='"+ input("Nouveau Population :")+"' WHERE nom='Auray';")
    resultat = curseur.execute(requete)
    
    conn.commit()  # Les modifications sont appliquées dans la BDD
    
    # 'commit()' est nécessaire pour les requêtes de modification
    

    curseur.close()  # fermeture du curseur
    conn.close()     # fermeture du connection
```