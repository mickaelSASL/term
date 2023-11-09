# BDD1 : Exercices - Corrigé

## 1. Les schémas relationnels

Une sandwicherie effectuant des livraisons à domicile dispose d’une base de données dont certains extraits sont présentés ci-dessous. 
La table `Sandwichs` comporte les informations relatives aux sandwichs proposés à la vente :

| Nom_Sandwich  | Prix  |
|---------------|-------|
| Cheeseburger  | 3.90  |
| Double cheese | 4.90  |
| Italien       | 4.90  |
| Foie gras     | 15.00 |

La table Clients comporte les informations relatives aux clients :

|   Nom	  | Prénom	|                 Adresse         	|Numéro_client|
|---------|---------|-----------------------------------|-------------|
|Bernard	|Alain	|9, rue Bienvenu, 13008 MARSEILLE	|      42     |
|Bernard	|Yves	|2, rue Vive la Joie, 13400 AUBAGNE	|      51     |

La table Commandes comporte les informations relatives aux commandes passées :

|Numéro_Client	|Nom_Sandwich	|Quantité |Numéro_Commande|    Date    |
|---------------|---------------|---------|---------------|------------|
|      42       |   Italien     |    2    |     12452	  | 2019-12-11 |
|      42       |	Foie gras   |	 1	  |     12452	  | 2019-12-11 |
|      51       | Cheeseburger  |	 4	  |     13301     | 2019-12-23 |

!!! Question "a. Une commande peut-elle comporter plusieurs sandwichs de types différents ?"  

??? note "Solution"

    Une commande peut comporter plusieurs sandwichs de types différents.  
    >    Exemple : la commande n°`12452` : `Italien` & `Foie gras`
 
!!! Question "b.	Quel est le schéma de la table Sandwichs ? de la table Clients ? de la table Commandes ?"  

??? note "Solution"

    table `Sandwichs` :  Sandwichs (Nom_Sandwich, Prix )  
    table `Clients` :  Clients (Nom, Prénom, Adresse, Numéro_client)  
    table `Commandes` : Commandes (Numéro_Client, Nom_Sandwich, Quantité, Numéro_Commande, Date)


!!! Question "c.	La table Sandwichs comporte-t-elle un attribut qui est clé primaire ? Un attribut qui clé étrangère ?"  

??? note "Solution"    

    La clé primaire de la table `Sandwichs` est `Nom_Sandwich`
    la table `Sandwichs` n'a pas de clé étrangère.

!!! Question "d.	Répondre aux mêmes questions pour les tables Clients et Commandes. En l’absence d’un attribut clé primaire, un couple ou un triplet d’attribut peut-il jouer ce rôle ?"  

??? note "Solution"

    La clé primaire de la table `clients` est `Numéro_client`
    La table `clients` n'a pas de clé étrangère.
 
    La table `Commandes` n'a pas d'attribut clé primaire mais le couple `(Numéro_Client, Numéro_Commande)` en forme une.
    Elle a une clé étrangère : `Numéro_Client`. 

!!! Question "e.	Cette base de données semble-t-elle bien modélisée ? Si ce n’est pas le cas, proposer des modifications. "  

??? note "Solution"

    Cette base de données semble bien modélisée. Les relations créées lui permettront de fonctionner. Cependant, la logique voudrait que l'on utilise, dans la table `Commandes`, un enregistrement par commande.  
    Son schéma de relation serait :  
    `Commandes ( 🔑Numéro_Commande, Numéro_Client, Liste_Sandwich, Liste_Quantité, Date )`


## 2. Modéliser une base de données

On souhaite modéliser, de manière nettement simplifiée, une base de données concernant les informations relatives à un forum hébergé sur Internet. Une première relation, Users, contient les informations relatives aux comptes des utilisateurs du forum : pseudonyme, adresse email, date d’enregistrement, droits (administrateurs, modérateur, etc.).

Une seconde relation, Posts, contient des informations relatives aux messages postés sur le forum : titre, contenu, date et heure du message, auteur.

!!! Question "a. Proposer un schéma relationnel permettant de représenter les utilisateurs. Donner un exemple d’enregistrement."

!!! Question "b. La relation Users comporte-t-elle une clé primaire ? Si oui, laquelle ?"

!!! Question "c. Proposer un schéma relationnel permettant de représenter les messages. Donner un exemple d’enregistrement."

!!! Question "d. La relation Posts comporte-t-elle une clé primaire ? Si oui, laquelle ? Comporte-t-elle une clé étrangère ? Si oui, laquelle ?"

!!! Question "e. On souhaite autoriser les utilisateurs à changer leur pseudonyme. Quelles adaptations des schémas relationnels seront nécessaires et pourquoi ?"

## 3. Création de base de données

#### a) Anciens élèves

On veut créer une petite base de données permettant de garder le contact avec nos copains de classe. On supposera qu'ils sont tous domicilies en France, qu'ils n'ont qu'un numéro de téléphone, mais éventuellement plusieurs adresses. On veut stocker les renseignements suivants : nom, prénom, sexe, date de naissance, numéro de téléphone, rue, numéro postal, ville, département et région.

!!! Question "Réalisez un schéma relationnel."

??? note "Solution"

    ![](Création BDD a.png)

#### b) Clients étrangers

On veut créer une base de données permettant de gérer les clients étrangers d'une entreprise et les pays de ces clients. La table des clients sera simplifiée et comportera leur nom, leur prénom, le pays de résidence et le solde de leur compte, dans la monnaie du pays.

On veut aussi que les clients aient la possibilité de faire des réclamations et que la base de données gère toutes ces réclamations pour chacun des clients.

!!! Question "Réalisez un schéma relationnel."

??? note "Solution"

    ![](Création BDD b.png)


#### c) Listes de classe

Une école veut informatiser ses listes de classe. Une classe est formée d'élevés (toujours les mêmes et un élevé n'appartient qu'à une seule classe). Il y a un enseignant de classe par classe. Un professeur peut enseigner plusieurs disciplines.

!!! Question "Réalisez un schéma relationnel."

??? note "Solution"

    ![](Création BDD c.png)