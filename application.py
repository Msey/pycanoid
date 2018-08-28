import pygame as pg
#import sys;

from player import Player
from missile import Missile
from brick import Brick

class Application:
    
    displaysize  = (400,400)

    @staticmethod
    def update_graphics(level, missile, player, screen):
        screen.fill([0,0,0])
        missile.update(screen)
        player.update(screen)
        for brick in level:
            brick.update(screen)
        pg.display.update()
        pg.display.flip()

    @staticmethod
    def update_colliders(level, missile, player, dt):
        missile.position(int(missile.x + missile.speedX * dt), int(missile.y + missile.speedY * dt))
        for brick in level:
            if (brick.collides(missile)):
                level.remove(brick) 
		if(player.collides(missile)):
                pass

    def main(self):
        player = None
        screen = None    

        pg.init()
        screen = pg.display.set_mode(Application.displaysize)

        player = Player(200)
        missile = Missile(200, 50)
        missile.speedX = missile.speedY = 1        
        level = []

        import random
        for x in range(0, 400, 10):
            for y in range(200, 400, 10):
                if (random.choice([1,2]) == 1):
                    level.append(Brick(x,y))

        while True:       
            dt = pg.time.Clock().tick(120)/5

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
                elif event.type == pg.MOUSEMOTION:
                     string = str(event.pos[0])
                     player.position(event.pos[0],0)
            
            Application.update_colliders(level, missile, player, dt)
            Application.update_graphics(level, missile, player, screen)

Application().main();