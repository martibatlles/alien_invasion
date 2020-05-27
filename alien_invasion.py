import sys
import pygame
from settings import Settings


class AlienInvasion:
    """Classe per a controlar el joc"""

    def __init__(self):
        """Inicialitza el joc i crea recursos"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        

    def run_game(self):
        """Fa fincionar el loop principal pel joc"""
        while True:
            # Mira els events del teclat i el ratolí.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit

            # Redibuixa la pantalla durant el loop
            self.screen.fill(self.settings.bg_color)

            # Mostra la finasta dibuixada més recent.
            pygame.display.flip()


def main():
    # Crea un objecte de classe AlienInvasion
    ai = AlienInvasion()
    ai.run_game()

if __name__ == "__main__":
    main()
