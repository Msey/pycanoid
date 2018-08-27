class Player:    
    import pygame as pg  

    collider = pg.Rect(0, 0, 0, 0)

    def __init__(self, x):
        Player.position(self,x)

    def update(self,screen):
        import pygame as pg           
        pg.draw.rect(screen, [100,255,170], self.collider, 2)    

    
    def position(self,x,y = 0):
        self.x = x
        self.y = y
        self.collider = [self.x, self.y, 50, 25]

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
                missile.speedY = 1
            elif (missile.y > self.collider[1]):
                    missile.speedY = -1
         return flag