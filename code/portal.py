import pygame
from settings import *
import os

# to je zadnja stvar, ki jo dodajam, dodal bom kodo, ki bo omogocila, da ta koda tece na kateremkoli racunalniku
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'graphics',
'port.png')

# ustvarim nov class
class Portal(pygame.sprite.Sprite):
    # pos = rabim pozicijo vseh spritov
    # groups = del katere skupine je sprite
    def __init__(self,pos,groups):
        # zastartam clas v vrstici 5 
        super().__init__(groups)
        # zato ker imamo je tukaj zgoraj znotraj oklepaja groups, lahko uporabim spodnja izraza, saj sta nujna za vsak sprite
        # tukaj hocem naloziti sliko, zato moram uporabiti pygame.image.load, ter dodati kje se nahaja in jo pretvoriti v obliko, 
        ## ki jo zaslon lahko prikaze
        self.image = pygame.image.load(image_path).convert_alpha()
        # topleft = position (pozicija)
        self.rect = self.image.get_rect(topleft = pos)
        # dolocil bom hitbox
        self.hitbox = self.rect.inflate(-32,-32)

        # dobil sem program, ki mi bo na zaslonu prikazoval koncni portal