from loops_demineur import *
from sys import setrecursionlimit
from os import environ


def demineur():  # Fonction gérant l'appel des boucles du jeu
    setrecursionlimit(10 ** 6)  # Augmentation de la récursion maximale à 1 million
    pg.init()  # Initialisation des variables pygame
    screen_x = 0
    screen_y = 30
    environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (screen_x, screen_y)  # Placement de la fenêtre dans le coin en haut à gauche de l'écran

    nbr_cases_x = 20  # Définition des paramètres par défaut du démineur
    nbr_cases_y = 20
    nbr_bombes = 45

    replay = True  # Tant que le joueur veut rejouer on parcours les boucles suivantes
    while replay:
        replay = False
        # boucle où l'utilisateur décide des paramètres du jeu par une interface graphique
        screen, nbr_cases_x, nbr_cases_y, nbr_bombes, solution, is_reveal, flags, screen, images, revealed_case, start = start_loop(nbr_cases_x, nbr_cases_y, nbr_bombes)

        if start:
            # boucle du jeu gérant l'entrée utilisateur et l'affichage de la grille
            result, nombre_coups, play_time = game_loop(screen, nbr_cases_x, nbr_cases_y, nbr_bombes, solution, is_reveal, flags, images, revealed_case)

            # boucle de fin de jeu où le joueur vois le résultat de la partie et les résultats sauvegardé des parties similaires
            replay = end_loop(screen, result, nombre_coups, play_time, nbr_cases_x * nbr_cases_y, nbr_bombes)


if __name__ == '__main__':
    demineur()
