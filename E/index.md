---
hide:
  - navigation
  - toc
---

# **Annales Sujets écrits**  

<a href="https://kxs.fr/sujets/terminale-ecrit" target="_blank">sujets</a>

<div id="result"></div>

<script>
fetch("https://kxs.fr/sujets/terminale-ecrit")
  .then(res => res.text())
  .then(html => {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, "text/html");

    const article = doc.querySelector("article");

    document.getElementById("result").innerHTML = article.outerHTML;
  })
  .catch(
