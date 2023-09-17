import pygame
pygame.init()

#Creates Window
win = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("dungeon_,master")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()        

#Class and stats for Hero 
class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.strength = 1
        self.inventory = 1
        self.walkCount = 0

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x,self.y))
        
def redrawGameWindow():
    man.draw(win)
    

    pygame.display.update()

       
    
man = Player(200,410,64,64)
#game set to run 
run = True
#Running loop 
while run:
    clock.tick(27)
    pygame.time.delay(100)

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
    elif keys[pygame.K_s] and man.y < 1080-man.height - man.vel:
        man.y += man.vel
        
    
    redrawGameWindow()
    win.fill((0,0,0))



#Quit
pygame.quit()

