Serveur MySQL : `192.168.1.50`  
base de données : villes  
utilisateur : Prénom  
mdp : Nom

Créer un utilisateur avec tous les droits sur une base de données :  
```SQL
CREATE USER 'user'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON villes.* TO 'user'@'%';
FLUSH PRIVILEGES;
```

Supprimer un utilisateur :  
```SQL
DROP USER 'user'@'%';
```

Modifier le mot de passe d'untuilisateur :  
```SQL
UPDATE mysql.user SET authentication_string=MD5("password") where User="user";
```

Afficher les droit d'un utilisateur :  
```SQL
SHOW GRANTS FOR 'user'@'%';
```
