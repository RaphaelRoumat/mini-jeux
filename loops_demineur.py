from manipulation_case import *
from creation_surfaces import *
from generateur_tableau_demineur import gen_tab_demineur
import pygame as pg
from gestion_scores import *


def start_loop(nbr_cases_x, nbr_cases_y, nbr_bomb):  # Boucle du menu de départ
    screen = pg.display.set_mode((500, 500))
    screen.fill((0, 0, 0))
    # récupération des composants du menu de départ
    play_button, menu_button, messages, difficulty_buttons, buttons_ad_10, buttons_ad_1, buttons_sub_10, buttons_sub_1, easy_start_button = create_start_menu(screen, nbr_cases_x, nbr_cases_y, nbr_bomb)

    easy_start = False  # Initialisation du départ rapide à faux
    start = False

    clock = pg.time.Clock()  # Initialisation de l'horloge régulant la vitesse de la boucle
    run = True
    while run:

        for event in pg.event.get():
            if event.type == pg.QUIT:  # gestion de l'évènement de fermeture de fenêtre
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos = pg.mouse.get_pos()  # Récupération des coordonnées de la souris
                coordx, coordy = pos
                clicked_button = False  # Passe à vraie si un bouton est appuyé

                for k in range(3):  # Gestion des boutons add 10
                    if buttons_ad_10[k].test_clicked(coordx, coordy):
                        clicked_button = True
                        if k < 2:  # Add 10 horizontale ou verticale
                            if k == 0:  # Add 10 horizontale
                                nbr_cases_x += 10
                                messages[0].change_message(f"longueur:{nbr_cases_x}")
                            else:  # Add 10 verticale
                                nbr_cases_y += 10
                                messages[1].change_message(f"largeur:{nbr_cases_y}")
                        else:  # Add 10 des bombes
                            if nbr_bomb + 10 < nbr_cases_x * nbr_cases_y:
                                nbr_bomb += 10
                                messages[2].change_message(f"bombes:{nbr_bomb}")
                        break

                if not clicked_button:
                    for k in range(3):  # Gestion des boutons add 1
                        if buttons_ad_1[k].test_clicked(coordx, coordy):
                            clicked_button = True
                            if k < 2:  # Add 1 horizontale ou verticale
                                if k == 0:  # Add 1 horizontale
                                    nbr_cases_x += 1
                                    messages[0].change_message(f"longueur:{nbr_cases_x}")
                                else:  # Add 1 verticale
                                    nbr_cases_y += 1
                                    messages[1].change_message(f"largeur:{nbr_cases_y}")
                            else:  # Add 1 des bombes
                                if nbr_bomb + 1 < nbr_cases_x * nbr_cases_y:
                                    nbr_bomb += 1
                                    messages[2].change_message(f"bombes:{nbr_bomb}")
                            break

                if not clicked_button:
                    for k in range(3):  # Gestion des boutons sub 10
                        if buttons_sub_10[k].test_clicked(coordx, coordy):
                            clicked_button = True
                            if k < 2:  # Sub 10 horizontale ou verticale
                                if k == 0:  # Sub 10 horizontale
                                    if nbr_cases_x - 10 >= 2:
                                        nbr_cases_x -= 10
                                    else:
                                        nbr_cases_x = 2
                                    messages[0].change_message(f"longueur:{nbr_cases_x}")

                                else:  # Sub 10 verticale
                                    if nbr_cases_y - 10 >= 2:
                                        nbr_cases_y -= 10
                                    else:
                                        nbr_cases_y = 2
                                    messages[1].change_message(f"largeur:{nbr_cases_y}")

                            else:  # Sub 10 des bombes
                                if nbr_bomb - 10 >= 2:
                                    nbr_bomb -= 10

                                else:
                                    nbr_bomb = 1
                                messages[2].change_message(f"bombes:{nbr_bomb}")

                            if nbr_bomb >= nbr_cases_x * nbr_cases_y:  # gestion du problème du nombre de bombe supérieur au nombre de cases
                                nbr_bomb = nbr_cases_x * nbr_cases_y - 2
                                messages[2].change_message(f"bombes:{nbr_bomb}")
                            break

                if not clicked_button:
                    for k in range(3):  # Gestion des boutons sub 1
                        if buttons_sub_1[k].test_clicked(coordx, coordy):
                            clicked_button = True
                            if k < 2:  # Sub 1 horizontale ou verticale
                                if k == 0:  # Sub 1 horizontale
                                    if nbr_cases_x - 1 >= 2:
                                        nbr_cases_x -= 1
                                    else:
                                        nbr_cases_x = 2
                                    messages[0].change_message(f"longueur:{nbr_cases_x}")

                                else:  # Sub 1 verticale
                                    if nbr_cases_y - 1 >= 2:
                                        nbr_cases_y -= 1
                                    else:
                                        nbr_cases_y = 2
                                    messages[1].change_message(f"largeur:{nbr_cases_y}")

                            else:  # Sub 1 des bombes
                                if nbr_bomb - 1 >= 2:
                                    nbr_bomb -= 1

                                else:
                                    nbr_bomb = 1
                                messages[2].change_message(f"bombes:{nbr_bomb}")

                            if nbr_bomb >= nbr_cases_x * nbr_cases_y:  # gestion du problème du nombre de bombe supérieur au nombre de cases
                                nbr_bomb = nbr_cases_x * nbr_cases_y - 2
                                messages[2].change_message(f"bombes:{nbr_bomb}")
                            break
                if not clicked_button:
                    for k in range(3):  # Gestion des boutons de difficulté
                        if difficulty_buttons[k].test_clicked(coordx, coordy):
                            clicked_button = True
                            if k == 0:  # Difficulté facile
                                nbr_bomb = int(nbr_cases_x * nbr_cases_y * 0.08)
                            elif k == 1:  # Difficulté intermédiaire
                                nbr_bomb = int(nbr_cases_x * nbr_cases_y * 0.13)
                            else:  # Difficulté intermédiare
                                nbr_bomb = int(nbr_cases_x * nbr_cases_y * 0.18)

                            if nbr_bomb < 1:
                                nbr_bomb = 1
                            messages[2].change_message(f"bombes:{nbr_bomb}")
                            break
                if not clicked_button:  # gestion du bouton et de l'affichage du début facile
                    if easy_start_button.test_clicked(coordx, coordy):
                        clicked_button = True
                        if easy_start:
                            easy_start = False
                            messages[3].change_message(f":non")
                        else:
                            easy_start = True
                            messages[3].change_message(f":oui")
                if not clicked_button:
                    if menu_button.test_clicked(coordx, coordy):
                        clicked_button = True
                        run = False
                        start = False
                if not clicked_button:  # gestion du bouton prévoquant le début de la partie
                    if play_button.test_clicked(coordx, coordy):
                        run = False
                        start = True
        clock.tick(60)  # Limitation à 60 tours de boucle par secondes
        pg.display.flip()  # Update de l'écran

    solution, is_reveal, flags = gen_tab_demineur(nbr_cases_x, nbr_cases_y, nbr_bomb)  # Création de la grille de démineur
    screen, images = create_surf(nbr_cases_x, nbr_cases_y)  # Création des surfaces du démineur
    if easy_start:  # Si easy_start est vraie on révèle une case sans bombes
        revealed_case = reveal_easy_start(screen, nbr_cases_x, nbr_cases_y, images, solution, is_reveal)
    else:
        revealed_case = 0
    return screen, nbr_cases_x, nbr_cases_y, nbr_bomb, solution, is_reveal, flags, screen, images, revealed_case, start


def game_loop(screen, nbr_cases_x, nbr_cases_y, nbr_bomb, solution, is_reveal, flags, images, revealed_case):  # Boucle du jeu
    nombre_coups = 0  # Initialisation du nombre de coups à 1
    nbr_cases = nbr_cases_y * nbr_cases_x

    # Récupération des afficheurs du jeu
    afficheur_bombes, afficheur_flags, timer = create_game_display(screen, nbr_cases_y, nbr_bomb)
    counter = 0  # Variable comptant le nombre de tour de boucle pour mettre à jour le timer
    clock = pg.time.Clock()

    defeat = False  # Variable indiquant si la partie est perdue ou non
    run = True
    while run:

        for event in pg.event.get():
            if event.type == pg.QUIT:  # Gestion de la fermeture de la fenêtre
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:  # Gestion du clique droit
                pos = pg.mouse.get_pos()
                coordx, coordy = pos
                coordx = coordx // 22  # Détermination des numéros de case en fonction des coordonnées de la souris
                coordy = coordy // 22  #
                if coordx < nbr_cases_x and coordy < nbr_cases_y:  # Ajout d'un drapeau si la souris est dans la grille
                    flag_case(screen, images, flags, is_reveal, [coordy, coordx])  # Ajout du drapeaux ou suppression si on drapeaux est déjà à ces coordonnées
                    afficheur_flags.change_message(f"{len(flags)} DRAPEAUX")  # Mise à jour de l'affichage du nombre de drapeaux

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # Gestion du clique gauche
                pos = pg.mouse.get_pos()
                coordx, coordy = pos
                coordx = coordx // 22  # Détermination des numéros de case en fonction des coordonnées de la souris
                coordy = coordy // 22  #
                if coordx < nbr_cases_x and coordy < nbr_cases_y:  # Révélation de la case si la souris est dans la grille
                    if not is_reveal[coordy][coordx]:  # Si la cases n'est pas déjà révéler on révèle la case
                        nombre_coups += 1  # Incrémentation du nombre de coups

                        # Révélation de la case, récupération de la défaite et du nombre de cases révélés
                        new_revealed_case, defeat = reveal_case(screen, nbr_cases_x, nbr_cases_y, images, solution, is_reveal, [coordy, coordx])
                        revealed_case += new_revealed_case  # Incrémentation du nombre de cases révélés

        if defeat or revealed_case == nbr_cases - nbr_bomb:  # Si l'on perd ou que la victoire est détecter la boucle s'arrête
            run = False
        clock.tick(60)
        counter += 1
        if counter == 60:  # Ajout d'une seconde au timer toutes les 60 frames
            counter = 0
            timer.add_1_sec()
        pg.display.flip()

    suivant_button = Button(screen, "SUIVANT", [timer.get_timer_y(), timer.get_timer_x()], pg.font.Font(os.path.join('ressources', 'crystal_font.ttf'), 20), (0, 0, 0), (255, 255, 255))
    run = True
    run = True
    while run:

        for event in pg.event.get():
            if event.type == pg.QUIT:  # Gestion de la fermeture de la fenêtre
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # Gestion du clique gauche
                pos = pg.mouse.get_pos()
                coordx, coordy = pos
                if suivant_button.test_clicked(coordx, coordy):
                    run = False
            clock.tick(60)
            pg.display.flip()
    return defeat, nombre_coups, timer.get_timer_time()


def end_loop(screen, defeat, nombre_coups, play_time, nbr_cases, nbr_bombes):  # Boucle de fin de partie

    width, height = screen.get_width(), screen.get_height()
    end_curtain_pos = 0
    stop_value = width/2

    clock = pg.time.Clock()
    replay = False
    run = True
    while run:  # Boucle créant un rideau de fin noire
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

        pg.draw.line(screen, (0, 0, 0), (end_curtain_pos, 0), (end_curtain_pos, height), 1)  # Traçage des lignes du rideau de fin
        pg.draw.line(screen, (0, 0, 0), (width - 1 - end_curtain_pos, 0), (width - 1 - end_curtain_pos, height))
        end_curtain_pos += 1

        if end_curtain_pos == stop_value:
            run = False
        clock.tick(120)
        pg.display.flip()

    scores_similaires = get_score(nbr_cases, nbr_bombes)  # Récupération des scores  des parties similaires
    screen = pg.display.set_mode((500, 500))  # Changement de taille de fenêtre

    # Récupération des composants du menu de fin
    replay_button, menu_button, messages_top5 = create_end_menu(screen, defeat, nombre_coups, play_time, scores_similaires, nbr_cases, nbr_bombes)  # création du menu de fin, boutons et message

    if not defeat:  # En cas de victoire un récupère le menu de sauvegarde de la partie

        # Récupération des composants du menu de sauvegarde
        add_record_button, name_field, name_message = create_add_record(screen, messages_top5[4].get_msg_y() + messages_top5[4].get_msg_height() + 10)

        # Définition des charactères acceptés pour le nom de la sauvegarde
        char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # Gestion du clique gauche
                pos = pg.mouse.get_pos()
                coordx, coordy = pos
                if replay_button.test_clicked(coordx, coordy):  # Bouton rejouer
                    run = False
                    replay = True
                elif menu_button.test_clicked(coordx, coordy):  # Bouton quitter
                    run = False
                    replay = False
                elif not defeat:  # En cas de victoire : gestion du menu de victoire
                    if add_record_button.test_clicked(coordx, coordy) and len(name_field.get_message()) > 0:  # Si le bouton de sauvegarde est cliqué et le nom de la sauvegarde n'est pas vide on lance la sauvegarde

                        add_record(nbr_cases, nbr_bombes, play_time, name_field.get_message())  # ajout de la partie à la database
                        update_scores(messages_top5, nbr_cases, nbr_bombes)  # Mise à jour du top 5
                        black = (0, 0, 0)
                        add_record_button.hide(black)  #
                        name_field.hide(black)  # disparition des composants du menu de sauvegarde
                        name_message.hide(black)  #
                        defeat = True  # Passage de defeat à True pour empêcher l'accés au menu de sauvegarde

            elif not defeat:
                if event.type == pg.KEYDOWN:  # Gestion des touches du clavier
                    if event.key == pg.K_BACKSPACE:  # Gestion de la touche d'éffacement
                        name_field.remove_last_char()  # Suppresion du dernier charactère du nom
                    elif event.unicode.upper() in char_list:  # Ajout du charactère de la touche s'il est dans la liste des charactère autorisés
                        name_field.add_char(event.unicode)

        clock.tick(60)
        pg.display.flip()

    return replay
