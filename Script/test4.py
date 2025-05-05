#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit

# === Constants ===
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 20
GRAVITY = 0.5
JUMP_FORCE = -7
MOVE_SPEED = 3
PROXIMITY_DISTANCE = 50

# === Initialization ===
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pointless Platformer!!")
clock = pygame.time.Clock()

# === Sprite Groups ===
todraw = pygame.sprite.Group()
plats = pygame.sprite.Group()

# === Platform Class ===
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, disappear=False):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.disappear = disappear
        self.visible = True
        plats.add(self)

    def update(self):
        if self.visible:
            screen.blit(self.image, self.rect.topleft)

# === Player Class ===
class Player(pygame.sprite.Sprite):
    def __init__(self, color, start_x=20, start_y=20):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect(topleft=(start_x, start_y))
        self.move_x = 0
        self.move_y = 0
        self.onground = False
        todraw.add(self)

    def update(self):
        self.rect.x += self.move_x
        xcoll(self)
        self.rect.y += self.move_y
        ycoll(self)
        screen.blit(self.image, self.rect.topleft)

# === Collision Handling ===
def xcoll(player):
    collision = [b for b in pygame.sprite.spritecollide(player, plats, False) if b.visible]
    for block in collision:
        if player.move_x > 0:
            player.rect.right = block.rect.left
        elif player.move_x < 0:
            player.rect.left = block.rect.right

def ycoll(player):
    collision = [b for b in pygame.sprite.spritecollide(player, plats, False) if b.visible]
    player.onground = False
    for block in collision:
        if player.move_y > 0:
            player.rect.bottom = block.rect.top
            player.onground = True
            player.move_y = 0
        elif player.move_y < 0:
            player.rect.top = block.rect.bottom
            player.move_y = 0

# === Disappearing Blocks Based on Proximity ===
def handle_proximity_blocks(player, proximity_blocks):
    for block in proximity_blocks:
        distance = pygame.math.Vector2(player.rect.center).distance_to(block.rect.center)
        block.visible = distance >= PROXIMITY_DISTANCE

# === Level Construction ===
def build():
    proximity_blocks = []
    level = [
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
        '#############################'
    ]

    for row_idx, row in enumerate(level):
        for col_idx, cell in enumerate(row):
            x = col_idx * BLOCK_SIZE
            y = row_idx * BLOCK_SIZE
            if cell == '#':
                Platform(x, y)
            elif cell == '%':
                block = Platform(x, y, disappear=True)
                proximity_blocks.append(block)
    return proximity_blocks

# === Gravity ===
def apply_gravity(player):
    if not player.onground:
        player.move_y += GRAVITY

# === Create Players and Level ===
player1 = Player("red")
player2 = Player("blue")
proximity_blocks = build()

# === Game Loop ===
while True:
    screen.fill((0, 0, 0))
    apply_gravity(player1)
    apply_gravity(player2)

    handle_proximity_blocks(player1, proximity_blocks)
    handle_proximity_blocks(player2, proximity_blocks)

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == KEYDOWN:
            # Player 1 Controls
            if event.key == K_UP and player1.onground:
                player1.move_y = JUMP_FORCE
            if event.key == K_LEFT:
                player1.move_x = -MOVE_SPEED
            if event.key == K_RIGHT:
                player1.move_x = MOVE_SPEED

            # Player 2 Controls
            if event.key == K_w and player2.onground:
                player2.move_y = JUMP_FORCE
            if event.key == K_a:
                player2.move_x = -MOVE_SPEED
            if event.key == K_d:
                player2.move_x = MOVE_SPEED

        if event.type == KEYUP:
            if event.key in (K_LEFT, K_RIGHT):
                player1.move_x = 0
            if event.key in (K_a, K_d):
                player2.move_x = 0

    # Update and Draw
    todraw.update()
    plats.update()
    pygame.display.update()
    clock.tick(60)
