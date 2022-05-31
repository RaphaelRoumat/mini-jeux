import pygame as pg


def reveal_solution(screen, nbr_cases_x, nbr_cases_y, solution, images):  # Fonction de révélation de toutes les cases
    for k in range(nbr_cases_y):
        for t in range(nbr_cases_x):
            screen.blit(images[solution[k][t]], (22*t, 22*k))


def reveal_case(screen, nbr_cases_x, nbr_cases_y, images, solution, is_reveal, coords):  # Fonction de révélation d'une case choisie
    revealed_case_counter = 0  # Initialisation à 0 du nombre de cases révélés par la fonction
    defeat = False
    y, x = coords[0], coords[1]
    if not is_reveal[y][x]:  # Si la case n'est pas déjà révélé
        is_reveal[y][x] = True  # Sauvegarde de la case comme révélé
        if solution[y][x] == -1:  # Si la case est une bombe
            is_reveal[y][x] = False  # Enlèvement de la sauvegarde comme révélé pour ne pas provoquer de victoire
            screen.blit(images[solution[y][x]], (x * 22, y * 22))  # Affichage d'une bombe à l'emplacement de la case
            clock = pg.time.Clock()
            for k in range(nbr_cases_y):  # Affichage de toutes les bombes au rythme de 20 par secondes
                for t in range(nbr_cases_x):
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            quit()
                    if solution[k][t] == -1 and not(k == y and t == x):
                        screen.blit(images[-1], (t * 22, k * 22))
                        clock.tick(20)
                        pg.display.flip()

            reveal_solution(screen, len(solution[0]), len(solution), solution, images)  # Révélation de toute la grille
            defeat = True  # Déclaration de la partie comme perdue

        elif solution[y][x] > 0:  # Si la case n'est pas une bombe ou un 0
            screen.blit(images[solution[y][x]], (x * 22, y * 22))  # Affichage de la case voulue
            revealed_case_counter += 1

        else:  # Si la case est un 0
            revealed_case_counter += 1
            screen.blit(images[solution[y][x]], (x * 22, y * 22))
            for i in range(-1, 2):  # Reveal des cases autour des cases 0 par récursivité
                for j in range(-1, 2):
                    if 0 <= y + i < nbr_cases_y and 0 <= x + j < nbr_cases_x:
                        temporaire, defeat = reveal_case(screen, nbr_cases_x, nbr_cases_y, images, solution, is_reveal, [y + i, x + j])
                        revealed_case_counter += temporaire
    return revealed_case_counter, defeat


def flag_case(screen, images, flags, is_reveal, coords):  # Fonction gérant l'affichage des drapeaux
    if coords not in flags:  # Si la case n'a pas déjà de drapeau
        if not is_reveal[coords[0]][coords[1]]:
            flags.append(coords)  # Ajout de la case à la liste des drapeaux
            screen.blit(images[-3], (coords[1]*22, coords[0]*22))  # Affichage d'un drapeau
    else:  # Si la case est un drapeau
        del flags[flags.index(coords)]  # Suppression de la case de la liste des drapeaux
        screen.blit(images[-2], (coords[1]*22, coords[0]*22))  # Affichage du case cachée à la place de l'ancien drapeau


def reveal_easy_start(screen, nbr_cases_x, nbr_cases_y, images, solution, is_reveal):  # Fonction jouant 1 coup automatique de départ pour l'utilisateur
    min_case = 9  # Iniatialisation du minimum à une valeur impossible
    coords = []
    for y in range(nbr_cases_y):  # Recherche de la case de plus basse proximité dans la grille
        for x in range(nbr_cases_x):
            if solution[y][x] < min_case and solution[y][x] != -1:
                coords = [y, x]
                min_case = solution[y][x]

    # révalation de la case choisie
    new_revealed_case, defeat = reveal_case(screen, nbr_cases_x, nbr_cases_y, images, solution, is_reveal, coords)
    return new_revealed_case
