import pygame
pygame.init()

#Creates Window
win = pygame.display.set_mode((1920,1200))
pygame.display.set_caption("dungeon_,master")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
char = pygame.image.load('standing.png')
bg = pygame.image.load('bg.jpeg')

clock = pygame.time.Clock()        

class Wall(object):
    def __init__(self,x, y, width_wall,height_wall):
        self.x = x 
        self.y = y
        self.width_wall = width_wall
        self.height_wall = height_wall

    def collide_with_player(self,player):
        if(self.x < player.x + player.width and
           self.x + self.width_wall > player.x and
           self.y < player.y + player.height and
           self.y + self.height_wall > player.y):
            pass

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def collide_with_player(self,player):
        if(self.x + self.radius > player.x and
           self.x - self.radius < player.x + player.width and
           self.y + self.radius > player.y and
           self.y - self.radius < player.y + player.height):
            pass

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y), self.radius)

#Class and stats for Hero 
class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.strength = 1
        self.inventory_space = 16
        self.walkCount = 0

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.left:
            win.blit(walkLeft[self.walkCount%3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount%3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x,self.y))
        
def redrawGameWindow():
    global walkCount
    win.blit(bg,(0,0))
    man.draw(win)
    

    pygame.display.update()

walls = []
wall1 = Wall(10, 20, 10, 20)
walls.append(wall1)

bullets = []    
man = Player(200,410,40,60)
#game set to run 
run = True
#Running loop 
while run:
    clock.tick(244)
    pygame.time.delay(100)

    for wall in walls:
        wall.collide_with_player(man)

    bullets_to_remove = []
    for bullet in bullets:
        bullet.collide_with_player(man)
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets_to_remove.append(bullet)

    for bullet in bullets:
        if bullet.x<500 and bullet.x > 0:
            bullet.x += bullet.vel
        else: 
            bullets.pop(bullets.index(bullet))

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_d] and man.x < 1920 - man.vel - man.width:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right=False
        man.left= False
    
    if keys[pygame.K_w] and man.y > man.vel:
        man.y -= man.vel
        man.up = True
    elif keys[pygame.K_s] and man.y < 1080 -man.height - man.vel:
        man.y += man.vel
        man.down = True

    if man.x < 0:
        man.x = 0
    if man.x > 1920 - man.width:
        man.x = 1920 - man.width
    if man.y < 0:
        man.y = 0
    if man.y > 1080 - man.height:
        man.y = 1080 -man.height
    
    redrawGameWindow()
    win.fill((0,0,0))



#Quit
pygame.quit()

