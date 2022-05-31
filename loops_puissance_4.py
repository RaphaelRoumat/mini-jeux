import os as os
from check_victory import start_check
from class_message import *
from class_button import *


def game_loop(screen):
    screen.fill((255, 255, 255))
    separator = pg.image.load(os.path.join('ressources', 'separator.png'))
    for k in range(7):
        screen.blit(separator, (k * 100, 100))
    red_coin = pg.image.load(os.path.join('ressources', 'red_coin.png'))
    yellow_coin = pg.image.load(os.path.join('ressources', 'yellow_coin.png'))

    coins_image = {
        "red": red_coin,
        "yellow": yellow_coin
    }

    coins = []
    for k in range(6):
        coins.append([])
        for _ in range(7):
            coins[k].append("none")

    column_count = [0, 0, 0, 0, 0, 0, 0]
    play_counter = 0

    current_player = "red"
    clock = pg.time.Clock()  # Initialisation de l'horloge régulant la vitesse de la boucle
    victory = False
    equality = False
    run = True
    while run:
        pos = pg.mouse.get_pos()  # Récupération des coordonnées de la souris
        for event in pg.event.get():
            if event.type == pg.QUIT:  # gestion de l'évènement de fermeture de fenêtre
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

                if column_count[pos[0]//100] < 6:
                    play_counter += 1
                    coins[5 - column_count[pos[0]//100]][pos[0]//100] = current_player
                    screen.blit(coins_image[current_player], ((pos[0]//100) * 100, 600 - column_count[pos[0]//100] * 100))
                    victory = start_check(5 - column_count[pos[0] // 100], pos[0] // 100, coins, current_player)

                    if not victory:
                        column_count[pos[0]//100] += 1

                        if current_player == "red":
                            current_player = "yellow"
                        else:
                            current_player = "red"

                        if play_counter == 42:
                            run = False
                            equality = True

                    else:
                        run = False

        pg.draw.rect(screen, (255, 255, 255), (0, 0, 700, 100))

        if not victory:
            screen.blit(coins_image[current_player], ((pos[0]//100) * 100, 0))

        clock.tick(60)  # Limitation à 60 tours de boucle par secondes
        pg.display.flip()
    return current_player, equality


def end_loop(screen, winner, equality):
    black = (0, 0, 0)
    back_ground_white = (255, 255, 255)
    font = pg.font.Font(os.path.join('ressources', 'crystal_font.ttf'), 20)

    if equality:
        text = "Egalite !"
    else:
        if winner == "red":
            text = "Victoire du joueur rouge !"
        else:
            text = "Victoire du joueur jaune !"

    affichage_victoire = Message(screen, text, [0, 0], font, back_ground_white, black)
    button_replay = Button(screen, "REJOUER", [affichage_victoire.get_msg_y() + affichage_victoire.get_msg_height() + 10, 0], font, black, back_ground_white)
    button_menu = Button(screen, "MENU", [button_replay.get_button_y() + button_replay.get_button_height() + 10, 0], font, black, back_ground_white)

    replay = False
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # gestion de l'évènement de fermeture de fenêtre
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos = pg.mouse.get_pos()  # Récupération des coordonnées de la souris
                coordx, coordy = pos

                if button_replay.test_clicked(coordx, coordy):
                    replay = True
                    run = False
                if button_menu.test_clicked(coordx, coordy):
                    replay = False
                    run = False

        pg.display.flip()

    return replay
