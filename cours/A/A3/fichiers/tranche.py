# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:46:34 2020

"""

        
def tranche(tab):
    n = len(tab)
    smax = tab[0]
    imax = jmax = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += tab[j]
            if s > smax:
                smax = s
                imax = i
                jmax = j
    return tab[imax:jmax+1]
        


def tranche_dpr(tab):
    def tranche_dpr_(tab, a, b):
        """
        Renvoie le couple (smax, tmax) où tmax est la tranche de tab[a:b]
        de somme maximale et smax la valeur de cette somme
        """
        # à compléter
        return # à compléter
    return tranche_dpr_(tab, 0, len(tab))[1]

#################################################
#                                               #
#                   TESTS                       #
#                                               #
#################################################


import tabletest as tt
import copy


def check_validity_for_tranche(solvers, tests):
    """
    Vérifie que tous les solveurs trouvent les mêmes résultats sur les tests proposés
    Modifié pour tranche car le test échouait en comparant les tranches [0, 1] et [1] 
    qui ont la même somme
    """
    
    res = []
    message = ""
    tests_cop = copy.deepcopy(tests)
    for t in tests_cop:
        res.append(solvers[0](t))
    for s in solvers[1:]:
        tests_cop = copy.deepcopy(tests)
        for i in range(len(tests_cop)):
            if sum(s(tests_cop[i])) != sum(res[i]): # ligne modifiée
                message += "Test failed on {} with solvers {} and {}".format(tests[i], solvers[0].__name__, s.__name__) + "\n"
    if message == "":
        print("Validity tests successful" + "\n")
    else:
        print(message)


def test_tranche_dpr():
    for nb in (20, 500):    
        print()
        print("Test avec des listes de {} nombres".format(nb))
        tests = tt.random_tests(-1000, 1000, nb, 100)
        check_validity_for_tranche([tranche, tranche_dpr], tests)
        tt.run_performance([tranche, tranche_dpr], tests)









