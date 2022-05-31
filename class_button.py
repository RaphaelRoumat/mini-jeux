import pygame as pg


class Button:  # Classe permettant l'implémentation d'un bouton basique

    def __init__(self, surface, text,  coords, font, font_color, bg_color):
        self.y = coords[0]
        self.x = coords[1]
        self.surface = surface
        self.text = text
        self.offset = 4

        text = font.render(text, True, font_color)

        # Affichage du bouton
        self.rect = (self.x, self.y, text.get_width() + self.offset * 2, text.get_height() + self.offset * 2)
        pg.draw.rect(surface, bg_color, self.rect)
        surface.blit(text, (self.x + self.offset, self.y + self.offset))
        pg.draw.rect(surface, (120, 120, 120), self.rect, 2)

    def hide(self, color):  # Fonction cachant le bouton dans la couleur voulue
        pg.draw.rect(self.surface, color, self.rect)
        pg.draw.rect(self.surface, color, self.rect, 2)

    def test_clicked(self, click_x, click_y):  # Fonction vérifiant si les coordonnées d'un click sont sur le bouton
        if self.x <= click_x <= self.x + self.rect[2] and self.y <= click_y <= self.y + self.rect[3]:
            return True
        else:
            return False

    def get_button_width(self):  # Fonctions renvoyants des informations sur le bouton
        return self.rect[2]

    def get_button_height(self):  #
        return self.rect[3]

    def get_button_x(self):  #
        return self.x

    def get_button_y(self):  #
        return self.y
