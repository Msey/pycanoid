import pygame as pg;
import sys;
#
from player import Player;
from missile import Missile;

class Application():

    player = None
    screen = None

    displaymode  = (400,400)


    def create_window(self):
        pg.init()
        screen = pg.display.set_mode(Application().displaymode)

        player = Player(200)
        missile = Missile(200, 50)


        while True:       

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
                elif event.type == pg.MOUSEMOTION:
                     string = str(event.pos[0])
                     player.position(event.pos[0],0)
                     screen.fill([0,0,0])
                     player.update(screen)
                     missile.update(screen)

            pg.display.update()
            pg.display.flip()

Application().create_window();