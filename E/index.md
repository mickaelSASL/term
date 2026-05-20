---
hide:
  - navigation
  - toc
---

# **Annales Sujets écrits**  

<a href="https://kxs.fr/sujets/terminale-ecrit" target="_blank">sujets</a>

<iframe src="https://kxs.fr/sujets/terminale-ecrit" width="100%" height="600px"></iframe>


<div id="contenu"></div>

<script>
fetch("https://kxs.fr/sujets/terminale-ecrit")
  .then(response => response.text())
  .then(data => {
    document.getElementById("contenu").innerHTML = data;
  });
</script>
