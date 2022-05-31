import pygame as pg


class Timer:  # Classe gérant un compteur de la forme h:mm:ss

    def __init__(self, surface, coords, font, font_color, bg_color):
        self.y = coords[0]
        self.x = coords[1]
        self.surface = surface

        self.font_color = font_color
        self.bg_color = bg_color
        self.offset = 5

        self.heures = 0
        self.minutes = 0
        self.secondes = 0
        self.time = 0

        self.text_temps = "00:00:00"  # Mise à 0 du temps de départ

        # Affichage du temps de départ
        self.font = font
        self.text = self.font.render(self.text_temps, True, self.font_color)
        self.rect = (self.x, self.y, self.text.get_width() + self.offset * 2, self.text.get_height() + self.offset * 2)

        pg.draw.rect(self.surface, self.bg_color, self.rect)
        self.surface.blit(self.text, (self.x + self.offset, self.y + self.offset))

    def add_1_sec(self):  # Fonction permettant d'ajouter une seconde au compteur et de mettre à jour l'affichage
        self.time += 1
        pg.draw.rect(self.surface, self.bg_color, self.rect)

        self.secondes += 1  # Incrémentation des variables gérant l'affichage des heures/minutes/secondes
        if self.secondes == 60:
            self.secondes = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.heures += 1

        if self.secondes < 10:  # Ajout d'un 0 au début du message si le nombre de fait pas deux chiffres
            text_secondes = f"0{self.secondes}"
        else:
            text_secondes = str(self.secondes)

        if self.minutes < 10:
            text_minutes = f"0{self.minutes}"
        else:
            text_minutes = str(self.minutes)

        if self.heures < 10:
            text_heures = f"0{self.heures}"
        else:
            text_heures = str(self.heures)

        # Affichage du nouveau temps
        self.text_temps = text_heures + ":" + text_minutes + ":" + text_secondes
        self.text = self.font.render(self.text_temps, True, self.font_color)
        self.rect = (self.x, self.y, self.text.get_width() + self.offset * 2, self.text.get_height() + self.offset * 2)
        pg.draw.rect(self.surface, self.bg_color, self.rect)
        self.surface.blit(self.text, (self.x + self.offset, self.y + self.offset))

    def get_timer_width(self):  # Fonctions renvoyants des informations sur le bouton
        return self.rect[2]

    def get_timer_height(self):  #
        return self.rect[3]

    def get_timer_x(self):  #
        return self.x

    def get_timer_y(self):  #
        return self.y

    def get_timer_time(self):  #
        return self.time
