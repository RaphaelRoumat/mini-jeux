import pygame as pg


class Message:  # Classe permettant d'afficher un message de la couleur voulue sur fond voulue dans la police voulue

    def __init__(self, surface, message, coords, font, font_color, bg_color):
        self.y = coords[0]
        self.x = coords[1]
        self.surface = surface

        self.font_color = font_color
        self.bg_color = bg_color
        self.message = message
        self.offset = 5

        self.font = font
        self.text = self.font.render(self.message, True, self.font_color)
        self.rect = (self.x, self.y, self.text.get_width() + self.offset * 2, self.text.get_height() + self.offset * 2)

        # Affichage du message
        pg.draw.rect(self.surface, self.bg_color, self.rect)
        self.surface.blit(self.text, (self.x + self.offset, self.y + self.offset))

    def hide(self, color):  # Fonction cachant le message dans la couleur voulue
        pg.draw.rect(self.surface, color, self.rect)

    def update_message(self):  # Fonction mettant à jour le message en fonction de la variable de classe self.message
        pg.draw.rect(self.surface, self.bg_color, self.rect)
        self.text = self.font.render(self.message, True, self.font_color)
        self.rect = (self.x, self.y, self.text.get_width() + self.offset * 2, self.text.get_height() + self.offset * 2)
        pg.draw.rect(self.surface, self.bg_color, self.rect)
        self.surface.blit(self.text, (self.x + self.offset, self.y + self.offset))

    def change_message(self, message):  # Fonction changeant la valeur de self.message par le texte voulue
        self.message = message
        self.update_message()

    def add_char(self, char):  # Fonction ajoutant le texte voulue à la fin du message
        self.message = self.message + char
        self.update_message()

    def remove_last_char(self):  # Fonction supprimant le dernier charactère du message
        self.message = self.message[:-1]
        self.update_message()

    def get_message(self):  # Fonctions renvoyants des informations sur le bouton
        return self.message

    def get_msg_width(self):  #
        return self.rect[2]

    def get_msg_height(self):  #
        return self.rect[3]

    def get_msg_x(self):  #
        return self.x

    def get_msg_y(self):  #
        return self.y
