# **TD - création d'une base de données**

## ^^Créer la base de données et des tables^^
### La base de données

!!! info
    
    Pour chaque création, vous pouvez le faire par l'interface graphique ou par une requête SQL.


Pour commencer, vous devez créer une base de données. (Après avoir choisi un nom, par exemple `db_livres.db`)

??? "Requête SQL"

    ```SQL
    CREATE DATABASE db_livres ;
    ```

### Les tables

Ensuite, on passe à la création de la table `LIVRES` avec les attributs suivants :
```SQL
id INT (clé primaire) 
titre TEXT
auteur TEXT
ann_publi INT
note INT 
```

??? "Requête SQL"

    ```SQL
    CREATE TABLE LIVRES (id INT, titre TEXT, id_auteur INT, ann_publi INT, note INT);
    ```

Comme indiqué dans la fenêtre, vous venez de créer votre première table.  

!!! Question "On recommence l'opération avec la table auteurs..."

    Créez une table `AUTEURS` avec les attributs suivants : 
    ```SQL
    id INT  (clé primaire)  
    titre TEXT  
    id_auteur INT  
    ann_publi INT  
    note INT
    ```

    ??? "Requête SQL"

        ```SQL
        CREATE TABLE AUTEURS
        (id INT, nom TEXT, prenom TEXT, ann_naissance INT, langue_ecriture TEXT);
        ```

## ^^Ajouter des données : **INSERT INTO**^^
Puis nous allons remplir ces tables avec les requêtes suivantes :

===! "Pour les auteurs"

    ```SQL
    INSERT INTO AUTEURS 
    (id,nom,prenom,ann_naissance,langue_ecriture)
    VALUES
    (1,'Orwell','George',1903,'anglais'),
    (2,'Herbert','Frank',1920,'anglais'),
    (3,'Asimov','Isaac',1920,'anglais'),
    (4,'Huxley','Aldous',1894,'anglais'),
    (5,'Bradbury','Ray',1920,'anglais'),
    (6,'K.Dick','Philip',1928,'anglais'),
    (7,'Barjavel','René',1911,'français'),
    (8,'Boulle','Pierre',1912,'français'),
    (9,'Van Vogt','Alfred Elton',1912,'anglais'),
    (10,'Verne','Jules',1828,'français');
    ```
=== "Pour les livres"

    ```SQL
    INSERT INTO LIVRES
    (id,titre,id_auteur,ann_publi,note)
    VALUES
    (1,'1984',1,1949,10),
    (2,'Dune',2,1965,8),
    (3,'Fondation',3,1951,9),
    (4,'Le meilleur des mondes',4,1931,7),
    (5,'Fahrenheit 451',5,1953,7),
    (6,'Ubik',6,1969,9),
    (7,'Chroniques martiennes',5,1950,8),
    (8,'La nuit des temps',7,1968,7),
    (9,'Blade Runner',6,1968,8),
    (10,'Les Robots',3,1950,9),
    (11,'La Planète des singes',8,1963,8),
    (12,'Ravage',7,1943,8),
    (13,'Le Maître du Haut Château',6,1962,8),
    (14,'Le monde des A',9,1945,7),
    (15,'La Fin de l'éternité',3,1955,8),
    (16,'De la Terre à la Lune',10,1865,10);
    ```

## ^^Interroger la base de données^^
Exécutons maintenant quelques requêtes :

===! "Sélection"

    Sélection de l'attribut `titre` dans la table `LIVRES`

    ```SQL
    SELECT titre FROM LIVRES
    ```

=== "Sélection avec filtre 1"

    ```SQL
    SELECT titre FROM LIVRES
    WHERE ann_publi = 1960
    ```

=== "Sélection avec filtre 2"

    ```SQL
    SELECT * FROM AUTEURS
    where nom='Asimov'
    ```

=== "Requête3"

    ```SQL
    SELECT * FROM LIVRES
    JOIN AUTEURS on livres.id_auteur=auteurs.id
    ```

=== "Requête4"

    ```SQL
    SELECT titre FROM LIVRES
    JOIN AUTEURS on livres.id_auteur=auteurs.id
    WHERE auteurs.nom='Asimov'
    ```

## ^^Manipuler les enregistrements^^
Insérer un nouvel enregistrement, supprimer un enregistrement et modifier un enregistrement
Comme nous avons créé cette base de données, nous en somme propriétaire et nous pouvons insérer un nouvel enregistrement et également en supprimer.

===! "Insérer un auteur"

    ```SQL
    INSERT INTO AUTEURS
    (id,nom,prenom,ann_naissance,langue_ecriture)
    VALUES
    (11,'Simmons','Dan',1948,'anglais')
    ```

=== "Insérer un livre"

    ```SQL
    INSERT INTO LIVRES
    (id,titre,id_auteur,ann_publi,note)
    VALUES
    (17,'Hypérion',11,1991,10)
    ```

=== "Modifier"

    ```SQL
    UPDATE LIVRES
    SET note=7
    WHERE titre = 'Hypérion'
    ```

=== "Supprimer"

    ```SQL
    DELETE FROM LIVRES
    WHERE titre='Hypérion'
    ```

## ^^Exercice^^

!!! Question "Écrire des requêtes pour :"  

    1. attribuer la note de 10 à tous les livres écrits par Asimov publiés après 1950  
    2. supprimer les livres publiés avant 1945

    ??? note "Solution"

        ===! "1"
        
            ```SQL
            UPDATE LIVRES JOIN AUTEURS ON livres.id_auteur=auteurs.id
            SET note=10
            WHERE auteurs.nom = 'Asimov' AND livres.ann_publi > 1950;
            ```

        === "2"
        
            ```SQL
            DELETE FROM LIVRES
            WHERE ann_publi < 1945;
            ```