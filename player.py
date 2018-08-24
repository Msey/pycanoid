class Player:    

    def __init__(self, x):
        Player.position(self,x)
        pass

    def update(self,screen):
        import pygame as pg        
        pg.draw.rect(screen, [0,255,0], [self.x, self.y, 50, 10], 1)    

    
    def position(self,x,y = 0):
        self.x = x
        self.y = y
