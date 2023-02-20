import pygame

class Ship():
    def __init__(self, alInv):
        self.screen = alInv.screen
        self.screenRect = alInv.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screenRect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
