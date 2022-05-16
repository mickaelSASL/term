# **LP2 : Récursivité**

<center><img src="https://files.realpython.com/media/Thinking-Recursively-in-Python_Watermarked.1825397c00ea.jpg" width="75%"></center>

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/Ect6H56Xs_BFukpJMa6EWzgBWLn1Vy5JNnC_DegXxIAwAQ?e=hW5xIJ
" target="_blank">Introduction<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>

<center><img src="https://imgs.xkcd.com/comics/fixing_problems.png"> </br><p style="font-size: 10px; font-style: italic;">source: xkcd.com</p></center>

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EWWmxvSBnVlDhG2RpujcvgoB8FYqPRunecyU5JMQ3oQd1g?e=u9WH92
" target="_blank">Document de cours<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>


<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EcicT0EDW_JBrn-mfqOH6KYBA6cmzVRkrcu8fgWFuG4bAg?e=nj5rq2" target="_blank">Exercices<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>

<center><img style="float: none;" src="https://www.ibm.com/ibm/history/ibm100/images/icp/E694819O58312C24/us__en_us__ibm100__fractals__video_mandelbrot_set_zoom__620x348.jpg" width="160px">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Mandel_zoom_04_seehorse_tail.jpg/1200px-Mandel_zoom_04_seehorse_tail.jpg" width="120px">
</center>

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20f%28n%29%3A%0A%20%20%20%20print%28n%29%0A%20%20%20%20if%20n%3C%3D%200%3A%0A%20%20%20%20%20%20%20%20print%28%22cas%20de%20base%22%29%0A%20%20%20%20%20%20%20%20return%200%20%20%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28f%22recursivit%C3%A9%20%7Bn%7D%22%29%0A%20%20%20%20%20%20%20%20return%20n%20%2B%20f%28n%20-%201%29%0A%20%20%20%20%0Af%282%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=20&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


![](exemple_recursif.jpg)

[Exercices - Corrigé](exo_corrigé.md)