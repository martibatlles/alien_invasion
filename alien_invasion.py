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
               
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Mou la nau cap a la dreta
            self.ship.moving_right = True
            
        elif event.key == pygame.K_LEFT:
            # Mou la nau cap a l'esquerra
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False




    def _update_screen(self):
        """Actualitza les imatges de la pantalla i les mostra"""
        # Redibuixa la pantalla durant el loop
        self.screen.fill(self.settings.bg_color)
             
        # Dibuixa la nau espacial a la pantalla
        self.ship.blitme()
 
        # Mostra la finestra dibuixada mes recent.
        pygame.display.flip()



    def run_game(self):
        """Fa funcionar el loop principal pel joc"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()



def main():
    # Crea un objecte de classe AlienInvasion
    ai = AlienInvasion()
    ai.run_game()

if __name__ == "__main__":
    main()
