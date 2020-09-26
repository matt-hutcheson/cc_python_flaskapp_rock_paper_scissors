import unittest

from src.game import Game
from src.player import Player

class TestGame(unittest.TestCase):
    # def setUp(self):
        # self.player_1_name = "Bob"
        # self.player_2_name = "Tom"

    def test_draw__None(self):
        test_player_1 = Player("Bob", "Rock")
        test_player_2 = Player("Tom", "Rock")
        test_game = Game(test_player_1, test_player_2)
        self.assertEqual(None, test_game.play_game(test_game))

    def test_rock_paper__player2wins(self):
        test_player_1 = Player("Bob", "Rock")
        test_player_2 = Player("Tom", "Paper")
        test_game = Game(test_player_1, test_player_2)
        self.assertEqual("Tom wins!", test_game.play_game(test_game))

    def test_rock_scissors__player1wins(self):
        test_player_1 = Player("Bob", "Rock")
        test_player_2 = Player("Tom", "Scissors")
        test_game = Game(test_player_1, test_player_2)
        self.assertEqual("Bob wins!", test_game.play_game(test_game))

    def test_paper_rock__player1wins(self):
        test_player_1 = Player("Bob", "Paper")
        test_player_2 = Player("Tom", "Rock")
        test_game = Game(test_player_1, test_player_2)
        self.assertEqual("Bob wins!", test_game.play_game(test_game))