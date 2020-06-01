class Settings:
    """La classe que controla la configuracio del joc Alien Invasion."""
    def __init__(self):
        """Inicialitza la configuracio del joc."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 666
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
