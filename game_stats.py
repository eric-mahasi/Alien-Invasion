class GameStats():
    """Track in-game stats."""

    def __init__(self, sett):
        """Initialize statistics"""
        self.sett = sett
        self.reset_stats()

        # Start the game in inactive state.
        self.game_active = False

        # High score never reset.
        self.highscore = 0

    def reset_stats(self):
        """Initialize variables that change in the course of the game.
        """
        self.ships_left = self.sett.ship_limit
        self.score = 0
        self.level = 1
