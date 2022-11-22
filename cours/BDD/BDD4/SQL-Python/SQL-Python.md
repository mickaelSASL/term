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
    requete=("UPDATE villes_france_free SET ville_population_2012='"+ input("Nouveau Population :")+"' WHERE nom='Auray';")
    resultat = curseur.execute(requete)
    
    conn.commit()  # Les modifications sont appliquées dans la BDD
    
    # 'commit()' est nécessaire pour les requêtes de modification
    

    curseur.close()  # fermeture du curseur
    conn.close()     # fermeture du connection
```