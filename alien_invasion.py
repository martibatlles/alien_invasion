import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Classe per a controlar el joc"""

    def __init__(self):
        """Inicialitza el joc i crea recursos"""
        pygame.init()
        self.settings = Settings()
        self.full_screen = False
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() 

    
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

        elif event.key == pygame.K_F11:
            if not self.full_screen:
                self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            else:
                self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            self.full_screen = not self.full_screen

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _fire_bullet(self):
        """Crea una nova bala i l'afegeix al grup de bales"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)



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
 
        # Dibuixa la bala
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Mostra la finestra dibuixada mes recent.
        pygame.display.flip()



    def run_game(self):
        """Fa funcionar el loop principal pel joc"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            
            # Elimina les bales que sobrepassen l'altura màximaç
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)


def main():
    # Crea un objecte de classe AlienInvasion
    ai = AlienInvasion()
    ai.run_game()

if __name__ == "__main__":
    main()
