#!/usr/bin/env python
# Imports
import pygame
from pygame.locals import *
from sys import exit
import level_selection

# Inizializziamo Pygame, schermo e clock
pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
level_select = 1  # Selezione del livello (1 o 2)

# Crea la finestra a schermo intero
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
clock = pygame.time.Clock()

# Creiamo i 2 principali gruppi di sprites
todraw = pygame.sprite.Group()
plats = pygame.sprite.Group()

# Classe per la creazione delle piattaforme
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        plats.add(self)

    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

# Classe giocatore
class Player(pygame.sprite.Sprite):
    move_x = 0
    move_y = 0
    onground = False

    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 40
        todraw.add(self)

    def update(self):
        self.rect.x += self.move_x
        xcoll(self)
        self.rect.y += self.move_y
        ycoll(self)
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("brown")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        todraw.add(self)
    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def exit(self, level_select):
        level_select += 1
        if level_select == 1:
            print("entrando livello 1")
            level, move = level_selection.level1()
        elif level_select == 2:
            print("entrando livello 2")
            level, move = level_selection.level2()
        elif level_select == 3:
            print("entrando livello 3")
            level, move = level_selection.level3()
        elif level_select == 4:
            print("entrando livello 4")
            level, move = level_selection.level4()
        elif level_select == 5:
            print("entrando livello 5")
            level, move = level_selection.level5()
        elif level_select == 6:
            print("entrando livello 6")
            level, move = level_selection.level6()
        elif level_select == 7:
            print("entrando livello 7")
            level, move = level_selection.level7()
        elif level_select == 8:
            print("entrando livello 8")
            level, move = level_selection.level8()
        elif level_select == 9:
            print("entrando livello 9")
            level, move = level_selection.level9()
        elif level_select == 10:
            print("entrando livello 10")
            level, move = level_selection.level10()
        elif level_select == 11:
            print("entrando livello 11")
            level, move = level_selection.level11()
        elif level_select == 12:
            print("entrando livello 12")
            level, move = level_selection.level12()
        elif level_select > 12:
            pygame.quit()
            exit()
        player1.rect.x = 50  # Posizione iniziale del primo giocatore
        player1.rect.y = 50
        player2.rect.x = 100  # Posizione iniziale del secondo giocatore
        player2.rect.y = 50
        print(level_select)
        return level, move, level_select, player1.rect.x, player1.rect.y, player2.rect.x, player2.rect.y

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("Red")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        todraw.add(self)

    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def morte(self,):
        player1.rect.x = 50  # Posizione iniziale del primo giocatore
        player1.rect.y = 50
        player2.rect.x = 100  # Posizione iniziale del secondo giocatore
        player2.rect.y = 50
        return player1.rect.x, player1.rect.y, player2.rect.x, player2.rect.y
    
class Water(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("Blue")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        todraw.add(self)

    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def morte(self,):
        player1.rect.x = 50  # Posizione iniziale del primo giocatore
        player1.rect.y = 50
        player2.rect.x = 100  # Posizione iniziale del secondo giocatore
        player2.rect.y = 50
        return player1.rect.x, player1.rect.y, player2.rect.x, player2.rect.y

class Acid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("Green")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        todraw.add(self)

    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def morte(self,):
        player1.rect.x = 50  # Posizione iniziale del primo giocatore
        player1.rect.y = 50
        player2.rect.x = 100  # Posizione iniziale del secondo giocatore
        player2.rect.y = 50
        return player1.rect.x, player1.rect.y, player2.rect.x, player2.rect.y
    
class MovingPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y, max_x, min_x, velocity):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("White")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.max_x = max_x
        self.min_x = min_x
        self.velocity = velocity
        self.back = 0
        plats.add(self)
    def update(self):    
        if self.rect.x >= self.max_x:
            self.back = 1
        elif self.rect.x <= self.min_x:
            self.back = 0

        if self.back == 0:
            self.rect.x += self.velocity
        elif self.back == 1:
            self.rect.x -= self.velocity
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Inv_Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("black")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        plats.add(self)

    def update(self):
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

# Costruire il livello
def build(level, move):
    door = []
    lava = []
    acqua = []
    acido = []
    mplats = []
    myx = 0
    myy = 0
    for r in level:
        for c in r:
            if c == ' ':
                pass
            elif c == '#':
                p = Platform(myx, myy)
            elif c == 'E':
                p = Door(myx, myy)
                door.append(p)
                print(p)
            elif c == 'L':
                p = Lava(myx, myy)
                lava.append(p)
            elif c == 'W':
                p = Water(myx, myy)
                acqua.append(p)
            elif c == 'A':
                p = Acid(myx, myy)
                acido.append(p)
            elif c == 'M':
                p = MovingPlatform(myx, myy, myx + move*50, myx, 3)
                mplats.append(p)
            elif c == 'm':
                p = MovingPlatform(myx, myy, myx + move*50, myx, 1)
                mplats.append(p)
            elif c == '?':
                p = Inv_Platform(myx, myy)
            myx += 50
        myy += 50
        myx = 0
    return door, lava, acqua, acido, mplats, level

# Simulazione di gravità
def gravity(player):
    if not player.onground:
        player.move_y += 0.2

# Creiamo i due giocatori
player1 = Player("red")
player2 = Player("blue")
player2.rect.x = 100  # Posizione iniziale del secondo giocatore
player2.rect.y = 50
player1.rect.x = 50  # Posizione iniziale del primo giocatore
player1.rect.y = 50

print(level_select)


if level_select == 1:
    level, move = level_selection.level1()
elif level_select == 2:
    level = level_selection.level2()
elif level_select == 3:
    level = level_selection.level3()
elif level_select == 4:
    level = level_selection.level4()
elif level_select == 5:
    level = level_selection.level5()
elif level_select == 6:
    level = level_selection.level6()
elif level_select == 7:
    level = level_selection.level7()
elif level_select == 8:
    level = level_selection.level8()
elif level_select == 9:
    level = level_selection.level9()
elif level_select == 10:
    level = level_selection.level10()
elif level_select == 11:
    level = level_selection.level11()
elif level_select == 12:
    level = level_selection.level12()

porte, lave, acque, acidi, mplats, level = build(level, move)
print(porte)

# Ciclo di gioco
while True:
    screen.fill((0, 0, 0))
    gravity(player1)
    gravity(player2)

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

    if porte and player1.rect.colliderect(porte[0].rect) and player2.rect.colliderect(porte[0].rect):
        level, move, level_select, player1.rect.x, player1.rect.y, player2.rect.x, player2.rect.y = porte[0].exit(level_select)
        plats.empty()
        todraw.empty()
        todraw.add(player1, player2)  # Riaggiungi i giocatori
        porte, lave, acque, acidi, level = build(level, move)
    for lava in lave:
        if player2.rect.colliderect(lava.rect):
            player1.rect.x, player1.rect.y, player2.rect.x, player2.rect.y = lava.morte()
            plats.empty()
            todraw.empty()
            todraw.add(player1, player2)
            porte, lave, acque, acidi, level = build(level, move)
    for acqua in acque:
        if player1.rect.colliderect(acqua.rect):
            player1.rect.x, player1.rect.y, player2.rect.x, player2.rect.y = acqua.morte()
            plats.empty()
            todraw.empty()
            todraw.add(player1, player2)
            porte, lave, acque, acidi, mplats, level = build(level, move)
    for acido in acidi:
        if player1.rect.colliderect(acido.rect) or player2.rect.colliderect(acido.rect):
            player1.rect.x, player1.rect.y, player2.rect.x, player2.rect.y = acido.morte()
            plats.empty()
            todraw.empty()
            todraw.add(player1, player2)
            porte, lave, acque, acidi, mplats, level = build(level, move)
        
    pygame.display.update()
    # Faccio in modo che il gioco non vada oltre i 60FPS
    clock.tick(60)
