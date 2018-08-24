class Missile:    

    def __init__(self, x, y):
        Missile.position(self,x,y)
        pass


    def update(self,screen):
        import pygame as pg        
        pg.draw.circle(screen, [255,255,255], [self.x, self.y], 10, 3)         


    def position(self,x,y):
        self.x = x
        self.y = y

