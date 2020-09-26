import unittest

from src.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.test_player = Player("Bob","Rock")

    def test_player_exists(self):
        self.assertEqual("Bob", self.test_player.name)
        self.assertEqual("Rock", self.test_player.choice)