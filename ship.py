import pygame


class Ship:
    """Una classe per controlar la nau espacial."""
    def __init__(self, ai_game):
        """Inicialitza la nau espacial i defineix la seva posició"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega la imatge i la posa dempeus.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Posa la nau espacial al centre de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Dibuixa la nau a la seva posició"""
        self.screen.blit(self.image, self.rect)
