import pygame as pg
import os
from class_button import Button
from class_message import Message
from class_timer import Timer


def create_surf(nbr_cases_x, nbr_cases_y):  # Fonction d'initialisation de l'écran pour la grille du démineur et des images permettant l'affichage de la grille

    width = nbr_cases_x * 22  # Calcul de la longueur nécessaire sachant qu'une case de démineur mesure 22 pixels
    height = nbr_cases_y * 22 + 35  # Ajout de 35 pixels à la largeur pour les afficheurs des bombes, drapeaux et du timer

    if width < 430:  # Les afficheurs font 430 pixels de longueur et donc la longueur doit faire au minimum 430 pixels
        width = 430

    screen = pg.display.set_mode((width, height))  # Création de la fenêtre en fonction de la taille de la zone de jeu en cases

    # loading des images dans l'ordre pour que leur valeur dans la matrice solution soit l'index dans le tableau des images
    # Si on veut afficher l'image du case avec 1 bombe à proximité l'image se trouve à l'index 1 du tableau des images
    image_0 = pg.image.load(os.path.join('ressources', '0.png'))
    image_1 = pg.image.load(os.path.join('ressources', '1.png'))
    image_2 = pg.image.load(os.path.join('ressources', '2.png'))
    image_3 = pg.image.load(os.path.join('ressources', '3.png'))
    image_4 = pg.image.load(os.path.join('ressources', '4.png'))
    image_5 = pg.image.load(os.path.join('ressources', '5.png'))
    image_6 = pg.image.load(os.path.join('ressources', '6.png'))
    image_7 = pg.image.load(os.path.join('ressources', '7.png'))
    image_8 = pg.image.load(os.path.join('ressources', '8.png'))
    image_flag = pg.image.load(os.path.join('ressources', 'flag.png'))
    image_hide = pg.image.load(os.path.join('ressources', 'hide.png'))
    image_bomb = pg.image.load(os.path.join('ressources', 'bomb.png'))

    images = [image_0, image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8, image_flag, image_hide, image_bomb]  # Tableau des images

    for y in range(nbr_cases_y):  # Affichage de la carte cachée
        for x in range(nbr_cases_x):
            screen.blit(image_hide, (22*x, 22*y))
    return screen, images


def create_end_menu(screen, result, nombre_coups, play_time, scores_similaires, nbr_cases, nbr_bombes):  # Fonction d'initialisation du menu de fin
    longueur_scores = len(scores_similaires)  # Calcul du nombre de scores pour les grilles avec nbr_cases cases et nbr_bombes bombes

    black = (0, 0, 0)  # Création des couleurs et polices nécessaire à la création des boutons
    back_ground_white = (255, 255, 255)
    font = pg.font.Font(os.path.join('ressources', 'crystal_font.ttf'), 20)

    # Création de l'affichage de la victoire ou défaite
    if result:
        result = "Defaite"
    else:
        result = "Victoire"

    message_offset = 10
    result_message = Message(screen, f"{result} en {nombre_coups} coups et {play_time} secondes !", [0, 0], font, back_ground_white, black)

    # Création des boutons Rejouer et Quitter
    replay_button = Button(screen, "REJOUER", [result_message.get_msg_y() + result_message.get_msg_height() + message_offset, 0],  font, black, back_ground_white)
    menu_button = Button(screen, "MENU", [replay_button.get_button_y() + replay_button.get_button_height() + message_offset, 0], font, black, back_ground_white)

    # Affichage du TOP 5 des scores
    message_classement = Message(screen, f"TOP 5 ({nbr_cases} cases {nbr_bombes} bombes):", [menu_button.get_button_y() + menu_button.get_button_height() + message_offset, 0], font, back_ground_white, black)
    messages_top5 = []

    if longueur_scores < 1:  # Si aucune sauvegarde existe dans le top 5 on écrit vide à la place du score d'une précédente partie
        text = " - vide"
    else:
        text = f" - {scores_similaires[0][2]}sec par {scores_similaires[0][3]} le {scores_similaires[0][4]}"

    messages_top5.append(Message(screen, text, [message_classement.get_msg_y() + message_classement.get_msg_height(), 0], font, back_ground_white, black))

    for k in range(1, 5):  # Affichage des 4 derniers scores du top 5
        if longueur_scores < k + 1:
            text = " - vide"
        else:
            text = f" - {scores_similaires[k][2]}sec par {scores_similaires[k][3]} le {scores_similaires[k][4]}"
        messages_top5.append(Message(screen, text, [messages_top5[k-1].get_msg_y() + messages_top5[k-1].get_msg_height(), 0], font, back_ground_white, black))

    return replay_button, menu_button, messages_top5


def create_add_record(screen, start_y):  # Création des messages et boutons nécessaire à la sauvegarde d'une partie finie
    black = (0, 0, 0)
    back_ground_white = (255, 255, 255)
    font = pg.font.Font(os.path.join('ressources', 'crystal_font.ttf'), 20)
    name_message = Message(screen, "Nom: ", [start_y, 0], font, back_ground_white, black)
    name_field = Message(screen, "", [start_y, name_message.get_msg_x() + name_message.get_msg_width() + 5], font, back_ground_white, black)
    add_record_button = Button(screen, "Sauvegarder", [name_message.get_msg_y() + name_message.get_msg_height() + 10, 0], font, black, back_ground_white)

    return add_record_button, name_field, name_message


def create_selector(screen, y_start, text, font, text_color, bg_color):  # Création des boutons et affichages nécessaire à la sélection d'un paramètre de départ

    button_add_10 = Button(screen, "+10", [y_start, 0], font, text_color, bg_color)
    button_add_1 = Button(screen, "+1", [button_add_10.get_button_y(), button_add_10.get_button_x() + button_add_10.get_button_width() + 5], font, text_color, bg_color)
    message = Message(screen, text, [button_add_10.get_button_y() + button_add_10.get_button_height() + 10, 0], font, bg_color, text_color)
    button_sub_10 = Button(screen, "-10", [message.get_msg_y() + message.get_msg_height() + 10, 0], font, text_color, bg_color)
    button_sub_1 = Button(screen, "-1", [button_sub_10.get_button_y(), button_sub_10.get_button_x() + button_sub_10.get_button_width() + 5], font, text_color, bg_color)

    return button_add_10, button_add_1, message, button_sub_10, button_sub_1


def create_start_menu(screen, nbr_cases_x, nbr_cases_y, nbr_bomb):  # Création du menu de départ permettant le paramétrage de la grille de démineur
    black = (0, 0, 0)
    back_ground_white = (255, 255, 255)
    font = pg.font.Font(os.path.join('ressources', 'crystal_font.ttf'), 20)

    # Création des boutons pour saisir la longueur de la grille
    horizontal_button_add_10, horizontal_button_add_1, horizontal_message, horizontal_button_sub_10, horizontal_button_sub_1 = create_selector(screen, 0, f"longueur:{nbr_cases_x}", font, black, back_ground_white)

    # Création des boutons pour saisir la largeur de la grille
    vertical_button_add_10, vertical_button_add_1, vertical_message, vertical_button_sub_10, vertical_button_sub_1 = create_selector(screen, horizontal_button_sub_10.get_button_y() + horizontal_button_sub_10.get_button_height() + 50, f"largeur:{nbr_cases_y}", font, black, back_ground_white)

    # Création des boutons pour saisir le nombre de bombes
    bomb_button_add_10, bomb_button_add_1, bomb_message, bomb_button_sub_10, bomb_button_sub_1 = create_selector(screen, vertical_button_sub_10.get_button_y() + vertical_button_sub_10.get_button_height() + 50, f"bombes:{nbr_bomb}", font, black, back_ground_white)

    # Affichage d'une ligne de séparation au milieu de l'écran
    pg.draw.line(screen, back_ground_white, (250, 0), (250, 500), 3)
    pg.display.flip()

    # Création des boutons permettant de choisir la difficulté
    hard_button = Button(screen, "DIFFICILE", [horizontal_message.get_msg_y(), 260], font, black, back_ground_white)
    medium_button = Button(screen, "MOYEN", [hard_button.get_button_y() + hard_button.get_button_height() + 10, 260], font, black, back_ground_white)
    easy_button = Button(screen, "FACILE", [medium_button.get_button_y() + medium_button.get_button_height() + 10, 260], font, black, back_ground_white)

    # Création du bouton et de l'affichage permettant de choisir si l'on veut un début simplifié ou non
    easy_start_button = Button(screen, "DEBUT FACILE", [easy_button.get_button_y() + easy_button.get_button_height() + 50, 260], font, black, back_ground_white)
    easy_start_msg = Message(screen, ":non", [easy_start_button.get_button_y(), easy_start_button.get_button_x() + easy_start_button.get_button_width() + 5], font, back_ground_white, black)

    # Création du bouton menu
    menu_button = Button(screen, "MENU", [easy_start_button.get_button_y() + easy_start_button.get_button_height() + 50, 260], font, black, back_ground_white)

    # Création du bouton provoquant le début de la partie
    play_button = Button(screen, "JOUER", [menu_button.get_button_y() + menu_button.get_button_height() + 50, 260], font, black, back_ground_white)

    # Rangement des boutons et affichages dans différents tableaux permettant une utilisation plus simple
    messages = [horizontal_message, vertical_message, bomb_message, easy_start_msg]
    difficulty_buttons = [easy_button, medium_button, hard_button]
    buttons_ad_10 = [horizontal_button_add_10, vertical_button_add_10, bomb_button_add_10]
    buttons_ad_1 = [horizontal_button_add_1, vertical_button_add_1, bomb_button_add_1]
    buttons_sub_10 = [horizontal_button_sub_10, vertical_button_sub_10, bomb_button_sub_10]
    buttons_sub_1 = [horizontal_button_sub_1, vertical_button_sub_1, bomb_button_sub_1]

    return play_button, menu_button, messages, difficulty_buttons, buttons_ad_10, buttons_ad_1, buttons_sub_10, buttons_sub_1, easy_start_button


def create_game_display(screen, nbr_cases_y, nbr_bomb):  # Création des afficheur présents pendant la partie
    font = pg.font.Font(os.path.join('ressources', 'crystal_font.ttf'), 20)

    # Création de l'afficheur du nombre de bombes dans la grille
    afficheur_bombes = Message(screen, f"{nbr_bomb} BOMBES", [nbr_cases_y * 22, 0], font, (255, 0, 0), (0, 0, 0))

    # Création de l'afficheur du nombre de drapeaux sur la grille
    afficheur_flags = Message(screen, "0 DRAPEAUX", [afficheur_bombes.get_msg_y(), afficheur_bombes.get_msg_width() + 20], font, (255, 0, 0), (0, 0, 0))

    # Création du timer
    timer = Timer(screen, [afficheur_flags.get_msg_y(), afficheur_flags.get_msg_x() + afficheur_flags.get_msg_width() + 20], font, (255, 0, 0), (0, 0, 0))

    return afficheur_bombes, afficheur_flags, timer
