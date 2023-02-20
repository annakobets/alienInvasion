import sys
import pygame


from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.screenWidth, self.settings.screenHeight))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._checkEvent()
            self._updateScreen()
            self.clock.tick(60)

    def _checkEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _updateScreen(self):
        self.screen.fill(self.settings.backColor)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    alInv = AlienInvasion()
    alInv.run_game()

