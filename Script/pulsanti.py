class Pulsante_Rosso(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("brown1")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.premuto = False
        todraw.add(self)
    
    def update(self):
        if self.premuto == False:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        self.premuto = False
    
    def pressione(self):
        self.premuto = True

class Pulsante_Blue(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("blue4")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.premuto = False
        todraw.add(self)
    
    def update(self):
        if self.premuto == False:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        self.premuto = False
    
    def pressione(self):
        self.premuto = True

class muro_rosso(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("brown1")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sbloccato = False
        plats.add(self)

    def update(self):
        if self.sbloccato == False:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        self.sbloccato = False

    def sblocca(self):
        self.sbloccato = True
        plats.remove(self)

class muro_blue(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("blue4")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sbloccato = False
        plats.add(self)
    def update(self):
        if self.sbloccato == False:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        plats.add(self)
        self.sbloccato = False

    def sblocca(self):
        self.sbloccato = True
        plats.remove(self)


#elif c == "P":
#    p = Pulsante_Rosso(myx, myy)
#    red_button.append(p)
#elif c =="p":
#    p = Pulsante_Blue(myx, myy)
#    blue_button.append(p)
#elif c =="r":
#    p = muro_rosso(myx,myy)
#    red_walls.append(p)
#elif c =="b":
#    p = muro_blue(myx,myy)
#    blue_walls.append(p)