import pygame


class Ship:
    """Una classe per controlar la nau espacial."""
    def __init__(self, ai_game):
        """Inicialitza la nau espacial i defineix la seva posicio"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega la imatge i obté el seu rectangle.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Posa la nau espacial al centre de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom


        self.x = float(self.rect.x)
        # Moviments
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left:
             self.rect.x -= self.settings.ship_speed
        # Actualitza el self.rect a partir del self.x
        self.rect.x = self.x
    def blitme(self):
        """Dibuixa la nau a la seva posicio"""
        self.screen.blit(self.image, self.rect)
