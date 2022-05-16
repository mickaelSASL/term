# ** BDD1 : Exercices - Corrigé**

## 1. Les schémas relationnels

> a. Une commande peut comporter plusieurs sandwichs de types différents.  
>    Exemple : la commande n°`12452` : `Italien` & `Foie gras`

___

> b. 
> table `Sandwichs` :  
> table `Clients` :  
> table `Commandes` :      

___

> c. La clé primaire de la table `Sandwichs` est `Nom_Sandwich`
>    la table `Sandwichs` n'a pas de clé étrangère.

___

> d. La clé primaire de la table `clients` est `Numéro_client`
>    La table `clients` n'a pas de clé étrangère.
> 
>    La table `Commandes` n'a pas d'attribut clé primaire mais le couple `(Numéro_Client, Numéro_Commande)` en forme une.
>    Elle a une clé étrangère : `Numéro_Client`. 

___

> e. Cette base de données semble bien modélisée. Les relations créées lui permettront de fonctionner. Cependant, la logique voudrait que l'on utilise, dans la table `Commandes`, un enregistrement par commande.  
>    Son schéma de relation serait :  
>    `Commandes ( 🔑Numéro_Commande, Numéro_Client, Liste_Sandwich, Liste_Quantité, Date )`


## 2. Modéliser une base de données

On souhaite modéliser, de manière nettement simplifiée, une base de données concernant les informations relatives à un forum hébergé sur Internet. Une première relation, Users, contient les informations relatives aux comptes des utilisateurs du forum : pseudonyme, adresse email, date d’enregistrement, droits (administrateurs, modérateur, etc.).

Une seconde relation, Posts, contient des informations relatives aux messages postés sur le forum : titre, contenu, date et heure du message, auteur.

a. Proposer un schéma relationnel permettant de représenter les utilisateurs. Donner un exemple d’enregistrement.

b. La relation Users comporte-t-elle une clé primaire ? Si oui, laquelle ?

c. Proposer un schéma relationnel permettant de représenter les messages. Donner un exemple d’enregistrement.

d. La relation Posts comporte-t-elle une clé primaire ? Si oui, laquelle ? Comporte-t-elle une clé étrangère ? Si oui, laquelle ?

e. On souhaite autoriser les utilisateurs à changer leur pseudonyme. Quelles adaptations des schémas relationnels seront nécessaires et pourquoi ?

## 3. Création de base de données

a) Anciens élèves

On veut créer une petite base de données permettant de garder le contact avec nos copains de classe. On supposera qu'ils sont tous domicilies en France, qu'ils n'ont qu'un numéro de téléphone, mais éventuellement plusieurs adresses. On veut stocker les renseignements suivants : nom, prénom, sexe, date de naissance, numéro de téléphone, rue, numéro postal, ville, département et région.

Réalisez un schéma relationnel.

b) Clients étrangers

On veut créer une base de données permettant de gérer les clients étrangers d'une entreprise et les pays de ces clients. La table des clients sera simplifiée et comportera leur nom, leur prénom, le pays de résidence et le solde de leur compte, dans la monnaie du pays.

On veut aussi que les clients aient la possibilité de faire des réclamations et que la base de données gère toutes ces réclamations pour chacun des clients.

Réalisez un schéma relationnel.

c) Listes de classe

Une école veut informatiser ses listes de classe. Une classe est formée d'élevés (toujours les mêmes et un élevé n'appartient qu'à une seule classe). Il y a un enseignant de classe par classe. Un professeur peut enseigner plusieurs disciplines.

Réalisez un schéma relationnel.