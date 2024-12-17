# **TD sur base distante**

Connecter vous sur la base de données `villes` située sur le serveur `192.168.2.239`, à l'aide de vos nom et prénom en respectant la syntaxe suivante :

* identifiant : `prénom` 
* mot de passe : `prénom`

> fichiers de la base de données :  
>
> * [table `departement.sql`](departement.sql)
> * [table `villes_france.sql`](villes_france.sql)



!!! Question "Exercice"
    - Ecrire les requêtes SQL permettant d’effectuer chacune des demandes suivantes :  

        
        ===! "❓ Question 1"
            Obtenir la liste des 10 villes les plus peuplées en 2012

        === "🧩 Réponse"
            ```SQL
            SELECT * 
            FROM `villes_france_free` 
            ORDER BY `ville_population_2012` DESC 
            LIMIT 10
            ```
        
        ===! "❓ Question 2"
            Obtenir la liste des 50 villes ayant la plus faible superficie

        === "🧩 Réponse"
            ```SQL
            SELECT * 
            FROM `villes_france_free` 
            ORDER BY `ville_surface` ASC 
            LIMIT 50
            ```

        ===! "❓ Question 3"
            Obtenir la liste des départements d’outres-mer, c’est-à-dire ceux dont le numéro de département commencent par “97”

        === "🧩 Réponse"
            ```SQL
            SELECT * 
            FROM `departement` 
            WHERE `departement_code` LIKE '97%'
            ```
            
        ===! "❓ Question 4"
            Obtenir le nom des 10 villes les plus peuplées en 2012, ainsi que le nom du département associé

        === "🧩 Réponse"
            ```SQL
            SELECT * 
            FROM `villes_france_free` 
            LEFT JOIN departement ON departement_code = ville_departement
            ORDER BY `ville_population_2012` DESC 
            LIMIT 10
            ```
            ```

        ===! "❓ Question 5"
            Obtenir la liste du nom de chaque département, associé à son code et du nombre de commune au sein de ces département, en triant afin d’obtenir en priorité les départements qui possèdent le plus de communes

        === "🧩 Réponse"
            ```SQL
            SELECT departement_nom, departement_code, COUNT(*) AS nbr_items 
            FROM `villes_france_free` 
            LEFT JOIN departement ON departement_code = ville_departement
            GROUP BY departement_nom, departement_code
            ORDER BY `nbr_items` DESC
            ```

        ===! "❓ Question 6"
            Obtenir la liste des 10 plus grands départements, en terme de superficie

        === "🧩 Réponse"
            ```SQL
            SELECT departement_nom, departement_code, SUM(`ville_surface`) AS dpt_surface 
            FROM `villes_france_free` 
            LEFT JOIN departement ON departement_code = ville_departement
            GROUP BY departement_nom, departement_code 
            ORDER BY dpt_surface  DESC
            LIMIT 10
            ```

        ===! "❓ Question 7"
            Compter le nombre de villes dont le nom commence par “Saint”

        === "🧩 Réponse"
            ```SQL
            SELECT COUNT(*) 
            FROM `villes_france_free` 
            WHERE `ville_nom` LIKE 'saint%'
            ```

        ===! "❓ Question 8"
            Obtenir la liste des villes qui ont un nom existants plusieurs fois, et trier afin d’obtenir en premier celles dont le nom est le plus souvent utilisé par plusieurs communes

        === "🧩 Réponse"
            ```SQL
            SELECT ville_nom, COUNT(*) AS nbt_item 
            FROM `villes_france_free` 
            GROUP BY `ville_nom` 
            ORDER BY nbt_item DESC
            ```


        ===! "❓ Question 9"
            Obtenir en une seule requête SQL la liste des villes dont la superficie est supérieur à la superficie moyenne

        === "🧩 Réponse"
            ```SQL
            SELECT * 
            FROM `villes_france_free` 
            WHERE `ville_surface` > (SELECT AVG(`ville_surface`) FROM `villes_france_free`)
            ```

        ===! "❓ Question 10"
            Obtenir la liste des départements qui possèdent plus de 2 millions d’habitants

        === "🧩 Réponse"
            ```SQL
            SELECT ville_departement, SUM(`ville_population_2012`) AS population_2012
            FROM `villes_france_free` 
            GROUP BY `ville_departement`
            HAVING population_2012 > 2000000
            ORDER BY population_2012 DESC
            ```

        ===! "❓ Question 11"
            Remplacez les tirets par un espace vide, pour toutes les villes commençant par “SAINT-” (dans la colonne qui contient les noms en majuscule)

        === "🧩 Réponse"
            ```SQL
            UPDATE `villes_france_free` 
            SET ville_nom = REPLACE(ville_nom, '-', ' ') 
            WHERE `ville_nom` LIKE 'SAINT-%'
            ```





!!! Info "Aide"

    ??? Tip "1. COUNT"

        La fonction `COUNT()` permet de compter le nombre d’enregistrement dans une table.
        ```SQL
        SELECT COUNT(*) FROM table
        ```
        Il est aussi possible de connaitre le nombre d’enregistrement sur une colonne en particulier. Les enregistrements qui possèdent la valeur nul ne seront pas comptabilisé. La syntaxe pour compter les enregistrement sur la colonne “nom_colonne” est la suivante :
        ```SQL
        SELECT COUNT(nom_colonne) FROM table
        ```

    ??? Tip "2. SUM"
    
        La fonction `SUM()` permet de calculer la somme totale d’une colonne contenant des valeurs numériques.
        ```SQL
        SELECT SUM(nom_colonne)
        FROM table
        ```

    ??? Tip "3. AVG"

        La fonction ``ÀVG()`` permet de calculer une valeur moyenne sur un ensemble d’enregistrement de type numérique et non nul.
        ```SQL
        SELECT AVG(nom_colonne) FROM nom_table
        ```

    ??? Tip "4. LIKE"

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

    ??? Tip "5. HAVING"  

        La condition `HAVING` est presque similaire à `WHERE` à la seule différence que `HAVING` permet de filtrer en utilisant des fonctions telles que `SUM()`, `COUNT()`, `AVG()`, `MIN()` ou `MAX()`.
        ```SQL
        SELECT colonne1, SUM(colonne2)
        FROM nom_table
        GROUP BY colonne1
        HAVING fonction(colonne2) operateur valeur
        ```

    ??? Tip "6. REPLACE"

        La fonction `REPLACE` permet de remplacer des caractères alphanumérique dans une chaîne de caractère. Cela sert particulièrement à mettre à jour des données dans une base de données ou à afficher des résultats personnalisés.
        ```SQL
        SELECT REPLACE('Hello tout le monde', 'Hello', 'Bonjour');
        ```

    ??? Tip "7. GROUP BY"

        Clause de l’instruction `SELECT` qui scinde le résultat de la requête en groupes de lignes, généralement pour effectuer ensuite une ou plusieurs agrégations sur chaque groupe. L’instruction `SELECT` retourne une ligne par groupe.
        ```SQL
        SELECT ColumnA, ColumnB FROM T GROUP BY ColumnA; 
        ```

        Résultat :
        ```SQL
        Bonjour tout le monde
        ```