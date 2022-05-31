from loops_puissance_4 import *


def puissance_4():
    pg.init()  # Initialisation des variables pygame
    screen_x = 0
    screen_y = 30
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (screen_x, screen_y)

    screen = pg.display.set_mode((700, 700))

    replay = True
    while replay:
        winner, equality = game_loop(screen)
        replay = end_loop(screen, winner, equality)


if __name__ == '__main__':
    puissance_4()
