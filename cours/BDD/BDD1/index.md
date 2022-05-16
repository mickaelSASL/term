# **BDD1 : Modèle relationnel, clé, schéma relationnel**

<center><img src="https://files.realpython.com/media/MySQL-and-Python_Watermarked.ea8870f8536c.jpg" width="75%"></center>

## ** 1. Qu'est-ce qu'une base de données ?**

Le développement des traitements informatiques nécessite **la manipulation de données de plus en plus nombreuses**.
Leur organisation et leur stockage constituent un enjeu essentiel de performance.

- L'an dernier nous avons abordé le stockage et la manipulation des données structurées à l'aide du format **CSV** (il en existe d'autres : **JSON, VCARD, XML, ...**).
Ces formats basés essentiellement sur du texte sont faciles à mettre en oeuvre et à utiliser mais ne sont **pas adaptés au traitement d'un grand nombre d'informations**, en particulier lorsque celles-ci se trouvent réparties dans plusieurs tables ou fichiers.  
*Imaginez une compagnie chargée de l'organisation de la circulation des trains sur le territoire national gérant les réservations et l'exploitation des trains avec des fichiers CSV !*

- Les **premières bases de données** sont apparues dans les **années 1960** et se sont développées en même temps que l'informatique.
Dans les années 1980 est apparu le **langage SQL** spécialement conçu pour faire des requêtes (sélectionner, filtrer, mettre à jour) sur les systèmes de bases de données.
Nous aborderons ce nouveau langage particulier dans cette partie.

- De nos jours les bases de données sont **omniprésentes**, en particulier sur le web. La plupart des sites, en particulier dans le commerce en ligne, y font largement appel.
**Elles jouent un rôle fondamental dans notre monde devenu numérique** où il est extrêmement facile de dupliquer l'information.

## ** 2. L'histoire des bases de données**
<center><iframe width="560" height="315" src="https://www.youtube.com/embed/iu8z5QtDQhY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>Le Machine Learning</iframe></center>


## ** 3. Les principes du modèle relationnel**
<center><iframe width="640" height="360" src="https://web.microsoftstream.com/embed/video/579b23f6-7722-407a-aa2d-20b5ce07133a?autoplay=false&showinfo=true" allowfullscreen style="border:none;"></iframe></center>


<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EUqXEQXV3bJDu-TAq5DzfqcBAxOxHufuc_aXTtYFD8c2BQ?e=KpHNK1
" target="_blank">Document de cours<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EXakBL7aGFBJkxOAq7NH3coBv5f_egIB-jdUy5seLVcQCg?e=RzFjlA" target="_blank">Fiche de révision<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>