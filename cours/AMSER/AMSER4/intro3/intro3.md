---
hide:
  - navigation
---

# Messages codés

## Codage de César avec changement de clé

Le calcul de la clé d'une lettre tient compte de la lettre précédente :

|    mot à coder                  |l |a |c |r |y |p |t |o |g |r |a |p |h |i |e |
|---------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
| codage sans clé                 |12|1 | 3|18|25|16|20|15|7 |18|1 |16|8 |9 |5 |
| clé 3 + code lettre précédente  |15|16| 7|24|46|44|39|38|25|28|22|20|27|20|17|
| modulo 26 (alphabet)            |15|16| 7|24|20|18|13|12|25|2 |22|20|1 |20|17|
| codage final                    |o |p |g |x |t |r |m |l |y |b |v |t |a |t |q |