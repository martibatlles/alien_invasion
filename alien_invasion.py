import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Classe per a controlar el joc"""

    def __init__(self):
        """Inicialitza el joc i crea recursos"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    
    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit


    def _update_screen(self):
        """Actualitza les imatges de la pantalla i les mostra"""
        # Redibuixa la pantalla durant el loop
        self.screen.fill(self.settings.bg_color)
             
        # Dibuixa la nau espacial a la pantalla
        self.ship.blitme()
 
        # Mostra la finestra dibuixada més recent.
        pygame.display.flip()



    def run_game(self):
        """Fa funcionar el loop principal pel joc"""
        while True:
            self._check_events()
            self._update_screen()



def main():
    # Crea un objecte de classe AlienInvasion
    ai = AlienInvasion()
    ai.run_game()

if __name__ == "__main__":
    main()
