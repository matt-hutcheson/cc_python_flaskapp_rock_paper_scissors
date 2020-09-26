import unittest

from src.game import Game
from src.player import Player

class TestGame(unittest.TestCase):
    # def setUp(self):
        # self.player_1_name = "Bob"
        # self.player_2_name = "Tom"

    def test_draw(self):
        test_player_1 = Player("Bob", "Rock")
        test_player_2 = Player("Tom", "Rock")
        test_game = Game(test_player_1, test_player_2)
        self.assertEqual(None, test_game.play_game(test_game))
