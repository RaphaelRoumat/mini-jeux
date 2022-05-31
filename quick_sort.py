
def swap(tableau, a, b):  # Fonction d'échange du trie récursif
    tableau[a], tableau[b] = tableau[b], tableau[a]


def quick_sort_scores(tableau, borne_inf, borne_sup):  # trie récursif classique modifié pour trié les sauvegardes en fonction de leur temps
    if borne_sup - borne_inf >= 1:
        pivot = (borne_sup + borne_inf) // 2
        swap(tableau, borne_inf, pivot)

        i = borne_inf + 1
        nbre_trie = 0

        while i <= borne_sup - nbre_trie:
            if tableau[i][2] > tableau[borne_inf][2]:
                swap(tableau, i, borne_sup - nbre_trie)
                nbre_trie += 1
            else:
                i += 1
        swap(tableau, borne_inf,  borne_sup - nbre_trie)
        pivot = borne_sup - nbre_trie
        quick_sort_scores(tableau, borne_inf, pivot - 1)
        quick_sort_scores(tableau, pivot + 1, borne_sup)
