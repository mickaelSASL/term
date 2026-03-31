```python
def plus_court_chemin_largeur(graphe, r_depart, r_arrivee):
    dict_chemins = {}
    L = [r_depart]
    sommets_marques = [r_depart]
    dict_chemins[r_depart] = [r_depart]

    for r in L:
        for s_r in graphe[r]:
            if not s_r in sommets_marques:
                sommets_marques.append(s_r)
                dict_chemins[s_r] = dict_chemins[r] + [s_r]
                if s_r == r_arrivee:
                    return dict_chemins[s_r]
                L.append(s_r)

```