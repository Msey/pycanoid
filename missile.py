class Missile:    

    speedX = 0
    speedY = 0

    import pygame as pg   
    collider = pg.Rect(0, 0, 0, 0)

    def __init__(self, x, y):
        Missile.position(self,x,y)
        pass


    def update(self,screen):
        import pygame as pg                
        pg.draw.rect(screen, [255,0,0], self.collider, 2)         


    def check_bounds(self, x, y):
        if (x >= 400 or x <= 0) :
            self.speedX*=-1
        if (y >= 400 or y <= 0) :
            self.speedY*=-1

    def position(self,x,y):        
        self.x = x
        self.y = y        
        self.collider = [self.x,self.y, 2,2]
        self.check_bounds(x, y)

