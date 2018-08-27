class Brick:


    rgb =[]

    def __init__(self, x, y):
        import random
        Brick.position(self,x,y)        
        self.rgb =[random.randrange(100,255),random.randrange(100,255),random.randrange(100,255)]
        pass


    def update(self,screen):
        import pygame as pg        
        pg.draw.rect(screen, self.rgb, self.collider, 1) 

    def position(self,x,y):
        self.x = x
        self.y = y
        self.collider = [self.x, self.y, 10, 10]

    def collides(self, missile):
         import pygame as pg

         flag = False

         if (pg.Rect(self.collider).colliderect(missile.collider)):
            flag = True

            if (missile.x < self.collider[0]):
                missile.speedX = -1
            elif (missile.x > self.collider[0]):
                    missile.speedX = 1
            if (missile.y > self.collider[1]):
                missile.speedY = -1
            elif (missile.y > self.collider[1]):
                    missile.speedY = 1
         return flag