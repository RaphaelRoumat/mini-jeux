from random import randint


def gen_tab_demineur(nbr_cases_x, nbr_cases_y, nbr_bomb):  # Fonction qui créer une grille de démineur en fonction des paramètres donnés
    tab_demineur = []  # Matrice contenant l'emplacement des bombes et la proximité de chaques cases d'une bombe sous la forme d'un entier: - 1 est une bombe, le reste de 0 à 8 est la proximité d'une bombe
    tab_case_reveal = []  # Matrice contenant des booléens indiquant si la case est révélé ou non
    liste_cases_libre = []  # Tableau contenant toutes les cases sans bombe
    N = nbr_cases_x * nbr_cases_y - 1  # Variable indiquant la fin du tableau list_cases_libre
    
    for k in range(nbr_cases_y):  # Initialisation des tableau et Matrices
        tab_demineur.append([])
        tab_case_reveal.append([])
        for t in range(nbr_cases_x):
            tab_demineur[k].append(0)
            tab_case_reveal[k].append(False)
            liste_cases_libre.append([k, t])

    for k in range(nbr_bomb):  # Création des bombes

        index_libre = randint(0, N)  # Sélection d'une case libre aléatoirement dans la liste liste_cases_libre
        y, x = liste_cases_libre[index_libre][0], liste_cases_libre[index_libre][1]  # Affectation des x et y en fonction des coords de la case libre
        liste_cases_libre[index_libre], liste_cases_libre[N] = liste_cases_libre[N], liste_cases_libre[index_libre]  # Mise à la fin de la case utilisé
        N -= 1  # Réduction de la longueur des cases libres pour rendre le dernier intouchable par l'aléatoire
        tab_demineur[y][x] = -1  # Placement de la bombe

        for i in range(-1, 2):  # Incrémentation des cases autour de la bombe posé si ce n'est pas une bombe
            for j in range(-1, 2):
                if 0 <= y + i < nbr_cases_y and 0 <= x + j < nbr_cases_x:
                    if tab_demineur[y + i][x + j] != -1:
                        tab_demineur[y + i][x + j] += 1

    return tab_demineur, tab_case_reveal, []
