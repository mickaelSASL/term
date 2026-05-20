---
hide:
  - navigation
  - toc
---

# **Annales Sujets écrits**  

<a href="https://kxs.fr/sujets/terminale-ecrit" target="_blank">sujets</a>


<div id="result"></div>

<script>
const url = "https://kxs.fr/sujets/terminale-ecrit";
const proxy = "https://thingproxy.freeboard.io/fetch/";

fetch(proxy + url)
  .then(res => res.text())
  .then(html => {
    const doc = new DOMParser().parseFromString(html, "text/html");

    const article = doc.querySelector("main article h1");

    document.getElementById("result").innerHTML =
      article ? article.outerHTML : "Introuvable";
  })
  .catch(err => {
    console.error(err);
    document.getElementById("result").innerText = "Erreur réseau";
  });
</script>
