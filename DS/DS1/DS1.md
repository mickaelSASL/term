---
hide:
  - navigation
---

# **DS1** 

## Thématiques abordées

## Sujet

## Corrigé

https://pythontutor.com/render.html#code=class%20Pile%28%29%3A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20self.valeurs%20%3D%20%5B%5D%0A%20%20%20%20%0A%20%20%20%20def%20empile%28self,%20element%29%3A%0A%20%20%20%20%20%20%20%20self.valeurs.append%28element%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20depile%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.valeurs.pop%28%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20est_vide%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.valeurs%20%3D%3D%20%5B%5D%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Adef%20produire_jeu%28n%29%3A%0A%20%20%20%20resultat%20%3D%20Pile%28%29%0A%20%20%20%20for%20i%20in%20range%28%20n%20%29%3A%0A%20%20%20%20%20%20%20%20resultat.empile%28n%20-%20i%29%0A%20%20%20%20return%20resultat%0A%0Adef%20scinder_jeu%28p,n%29%20%3A%0A%20%20%20%20m1%20%3D%20Pile%28%29%0A%20%20%20%20m2%20%3D%20Pile%28%29%0A%20%20%20%20for%20i%20in%20range%28int%28n/2%29%29%3A%0A%20%20%20%20%20%20%20%20m1.empile%28p.depile%28%29%29%0A%20%20%20%20for%20i%20in%20range%28int%28n/2%29%29%3A%0A%20%20%20%20%20%20%20%20m2.empile%28p.depile%28%29%29%0A%20%20%20%20return%20m1,%20m2%0A%0Adef%20recombiner%28m1,%20m2%29%20%3A%0A%20%20%20%20resultat%20%3D%20Pile%28%29%0A%20%20%20%20while%20not%20m1.est_vide%28%29%3A%0A%20%20%20%20%20%20%20%20resultat.empile%28m1.depile%28%29%29%0A%20%20%20%20%20%20%20%20resultat.empile%28m2.depile%28%29%29%0A%20%20%20%20return%20resultat%0A%0A%0Adef%20faro%28p,%20n%29%20%3A%0A%20%20%20%20m1,%20m2%20%3D%20scinder_jeu%28p,%20n%29%0A%20%20%20%20return%20recombiner%28m1,%20m2%29%0A%20%20%20%20%0An%20%3D%206%0Ajeu%20%3D%20produire_jeu%28n%29%0Afaro%28jeu,%20n%29&cumulative=false&curInstr=138&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false
