import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Una classe que simula una bala disparada per la nau"""

    def __init__(self, ai_game):
        """Crea la bala i la posa a la seva posició"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Crea la bala a les coordenades (0, 0) i després la mou a les coordenades correctes
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Agafa la posició de la bala i la introdueix en un float
        self.y = float(self.rect.y)


    def update(self):
        """Mou la bala cap amunt de la pantalla"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y


    def draw_bullet(self):
        """Dibuixa la bala a la pantalla"""
        pygame.draw.rect(self.screen, self.color, self.rect)
