print("\nNSI Partie Pratique - SUJET nº04\nBooleans/conditions et ...\n------------------------------------------\n\n• Exo 1 -->")

def effectif_notes(notes_eval:list)->list:
    liste = [0 for i in range(11)]
    for i in notes_eval:liste[i]+=1
    return liste
def notes_triees(tab:list)->list:
    liste = []
    for i in range(11): 
        for j in range(tab[i]):liste.append(i)
    return liste

def notes_triees1(tab:list)->list: return [i for i in range(11) for j in range(tab[i])]

notes_eval = [2,0,5,9,6,9,10,5,7,9,9,5,0,9,6,5,4]
eff = effectif_notes(notes_eval)
#tests
print(eff)
print(notes_triees1(eff))

print("• Exo 2 -->") 
def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)
def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin == '0':
            return 0
        else:
            return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit
#tests
print( dec_to_bin(25))
print(bin_to_dec('101010'))