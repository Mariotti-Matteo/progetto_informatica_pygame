#!/usr/bin/env python
# Imports
import pygame
from pygame.locals import *
from sys import exit

# Inizializziamo Pygame, schermo e clock
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Pointless Platformer!!")
clock = pygame.time.Clock()

# Creiamo i 2 principali gruppi di sprites
todraw = pygame.sprite.Group()
plats = pygame.sprite.Group()

# Classe per la creazione delle piattaforme
class Platform(pygame.sprite.Sprite):   
    def __init__(self, x, y, disappear=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.disappear = disappear  # Indica se il blocco può scomparire
        self.visible = True  # Stato di visibilità del blocco
        plats.add(self)

    def update(self):
        if self.visible:
            screen.blit(self.image, (self.rect.x, self.rect.y))


# Classe giocatore
class Player(pygame.sprite.Sprite):
    move_x = 0
    move_y = 0
    onground = False

    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
        todraw.add(self)

    def update(self):
        self.rect.x += self.move_x
        xcoll(self)
        self.rect.y += self.move_y
        ycoll(self)
        screen.blit(self.image, (self.rect.x, self.rect.y))

# Le collisioni vengono calcolate separatamente sull'asse x ed y
def xcoll(player):
    collision = pygame.sprite.spritecollide(player, plats, False)
    for block in collision:
        if player.move_x > 0:
            player.rect.right = block.rect.left
        if player.move_x < 0:
            player.rect.left = block.rect.right

def ycoll(player):
    collision = pygame.sprite.spritecollide(player, plats, False)
    player.onground = False
    for block in collision:
        if player.move_y == 0:
            player.onground = True
        if player.move_y < 0:
            player.rect.top = block.rect.bottom
            player.move_y = 0
            player.onground = False
        if player.move_y > 0:
            player.rect.bottom = block.rect.top
            player.onground = True

# Funzione per gestire la scomparsa del blocco "%" quando un player si avvicina
def handle_proximity_blocks(player, proximity_blocks):
    for block in proximity_blocks:
        distance = pygame.math.Vector2(player.rect.center).distance_to(block.rect.center)
        if distance < 50:  # Scompare se il giocatore è entro 50 pixel
            block.visible = False
        else:
            block.visible = True



# Costruire il livello
def build():
    proximity_blocks = []  # Lista dei blocchi "%"
    myx = 0
    myy = 0

    # level = [
    #     '###########################',
    #     '#            #            #',
    #     '#            #######      #',
    #     '#                      ####',
    #     '#   ##            ##      #',
    #     '#  ####      #########    #',
    #     '###########################']
    
    level=[
            '#############################',
            '#       #                   #',
            '#            ########       #',
            '#    #                     ##',
            '#             #         #####',
            '#        #             #    #',
            '#   ##             ##      ##',
            '#  ####      ## ####### #  ##',
            '#########################%###',
            '#     #                     #',
            '#   #    #    #    ##########',
            '#  ###########   #      #####',
            '##    #   #   ##########    #',
            '#       #                   #',
            '###     #        #          #',
            '#############################']

    for r in level:
        for c in r:
            if c == ' ':
                pass
            elif c == '#':
                Platform(myx, myy)
            elif c == '%':  # Blocchi che scompaiono quando un player si avvicina
                block = Platform(myx, myy, disappear=True)
                proximity_blocks.append(block)
            myx += 20
        myy += 20
        myx = 0
    return proximity_blocks

# Simulazione di gravità
def gravity(player):
    if not player.onground:
        player.move_y += 0.5

# Creiamo i due giocatori
player1 = Player("red")
player2 = Player("blue")
proximity_blocks = build()

# Ciclo di gioco
while True:
    screen.fill((0, 0, 0))
    gravity(player1)
    gravity(player2)

    # Gestione della scomparsa dei blocchi "%" in base alla vicinanza
    handle_proximity_blocks(player1, proximity_blocks)
    handle_proximity_blocks(player2, proximity_blocks)

    # Ciclo eventi
    for event in pygame.event.get():
        if event.type == QUIT:  # Uscita
            exit()
        if event.type == KEYDOWN:  # Viene premuto un tasto
            # Controllo per il primo giocatore
            if event.key == K_UP:
                if player1.onground:
                    player1.move_y = -7
                    player1.onground = False
            if event.key == K_LEFT:
                player1.move_x = -3
            if event.key == K_RIGHT:
                player1.move_x = 3
            
            # Controllo per il secondo giocatore
            if event.key == K_w:
                if player2.onground:
                    player2.move_y = -7
                    player2.onground = False
            if event.key == K_a:
                player2.move_x = -3
            if event.key == K_d:
                player2.move_x = 3

        if event.type == KEYUP:  # Viene rilasciato un tasto
            if event.key == K_LEFT:
                player1.move_x = 0
            if event.key == K_RIGHT:
                player1.move_x = 0
            # Controlli per il secondo giocatore
            if event.key == K_a:
                player2.move_x = 0
            if event.key == K_d:
                player2.move_x = 0

    # Aggiorna tutte le sprites e lo schermo
    todraw.update()
    plats.update()
    pygame.display.update()
    # Faccio in modo che il gioco non vada oltre i 60FPS
    clock.tick(60)
