from demineur_start import demineur
from puissance4_start import puissance_4
import os as os
import pygame as pg
from class_button import Button


def main():
    pg.init()  # Initialisation des variables pygame
    screen_x = 0
    screen_y = 30
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (screen_x, screen_y)
    screen = pg.display.set_mode((300, 150))
    black = (0, 0, 0)
    back_ground_white = (255, 255, 255)
    font = pg.font.Font(os.path.join('ressources', 'crystal_font.ttf'), 20)

    demineur_button = Button(screen, "DEMINEUR", [
                             0, 0], font, black, back_ground_white)
    puissance_4_button = Button(screen, "PUISSANCE 4", [demineur_button.get_button_y(
    ) + demineur_button.get_button_height() + 5, 0], font, black, back_ground_white)

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # gestion de l'évènement de fermeture de fenêtre
                quit()

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos = pg.mouse.get_pos()  # Récupération des coordonnées de la souris
                coordx, coordy = pos

                if demineur_button.test_clicked(coordx, coordy):
                    demineur()
                    screen = pg.display.set_mode((300, 150))
                    demineur_button = Button(screen, "DEMINEUR", [
                                             0, 0], font, black, back_ground_white)
                    puissance_4_button = Button(screen, "PUISSANCE 4", [demineur_button.get_button_y(
                    ) + demineur_button.get_button_height() + 5, 0], font, black, back_ground_white)

                if puissance_4_button.test_clicked(coordx, coordy):
                    puissance_4()
                    screen = pg.display.set_mode((300, 150))
                    demineur_button = Button(screen, "DEMINEUR", [
                                             0, 0], font, black, back_ground_white)
                    puissance_4_button = Button(screen, "PUISSANCE 4", [demineur_button.get_button_y(
                    ) + demineur_button.get_button_height() + 5, 0], font, black, back_ground_white)

        pg.display.flip()


if __name__ == '__main__':
    main()
