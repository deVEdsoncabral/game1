

import pygame

WIDTH = 1200
HEIGTH =  600
GAME_SPEED = 30
SPEED = 10
GROUND_WIDTH = 2* WIDTH
GROUND_HEIGTH = 30

class Player (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_run = [pygame.image.load('./sprites/Run__000.png').convert_alpha(),
                          pygame.image.load('./sprites/Run__001.png').convert_alpha(),
                          pygame.image.load('./sprites/Run__002.png').convert_alpha(),
                          pygame.image.load('./sprites/Run__003.png').convert_alpha(),
                          pygame.image.load('./sprites/Run__004.png').convert_alpha(),
                          pygame.image.load('./sprites/Run__005.png').convert_alpha(),
                          pygame.image.load('./sprites/Run__006.png').convert_alpha(),
                          pygame.image.load('./sprites/Run__007.png').convert_alpha(),
                          pygame.image.load('./sprites/Run__008.png').convert_alpha(),
                          pygame.image.load('./sprites/Run__009.png').convert_alpha()
                          ]
        self.image = pygame.image.load('./sprites/Run__000.png').convert_alpha()
        self.rect =pygame.Rect(100, 100, 100, 100)
        self.mask = pygame.mask.from_surface(self.image)
        self.current_image = 0

    def update(self, *args):
        def move_player(self):
            key= pygame.key.get_pressed()
            if  key[pygame.K_d]:
                self.rect[0] += GAME_SPEED
            if key [pygame.K_a]:
                self.rect[0] -= GAME_SPEED    
            self.current_image = (self.current_image + 1) % 10
            self.image = self.image_run[self.current_image]
            self.image = pygame.transform.scale(self.image,[100,100])
        move_player(self)
        self.rect[1] += SPEED

        def Fly(self):
            key = pygame.key.get_pressed()
            if key [pygame.K_SPACE]:
                self.rect[1] -= 30
                self.image = pygame.image.load('./sprites/Fly.png').convert_alpha()
                self.image = pygame.transform.scale(self.image,[100,100])    
                print("Fly")
        Fly(self)
        
       
class Ground(pygame.sprite.Sprite):
    def __init__(self,xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./sprites/ground.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,[GROUND_WIDTH, GROUND_HEIGTH])
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = HEIGTH - GROUND_HEIGTH

    def update(self, *args):
        self.rect[0] -= GAME_SPEED

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])


pygame.init()
game_window = pygame.display.set_mode([WIDTH, HEIGTH])
pygame.display.set_caption('jogo 01')

BACKGRAUND = pygame.image.load('./sprites/background_03.jpg').convert_alpha()
BACKGRAUND = pygame.transform.scale(BACKGRAUND,[WIDTH,HEIGTH])

playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)


GroundGroup = pygame.sprite.Group()
for i in range(2):
    ground = Ground(WIDTH * i)
    GroundGroup.add(ground)

clock=pygame.time.Clock()
gameLoop = True
def draw():
    playerGroup.draw(game_window)
    GroundGroup.draw(game_window)
def update():
    playerGroup.update()
    GroundGroup.update()
    clock == clock
while gameLoop:
    clock.tick(30)
    game_window.blit(BACKGRAUND,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    if is_off_screen(GroundGroup.sprites()[0]):
        GroundGroup.remove(GroundGroup.sprites()[0])
        newGround = Ground(WIDTH - 30)
        GroundGroup.add(newGround)
    if pygame.sprite.groupcollide(playerGroup , GroundGroup,False,False):
        SPEED = 0
        print('collision')  
    else:
        SPEED = 10         
    update()
    draw()        
    pygame.display.update()
    
    