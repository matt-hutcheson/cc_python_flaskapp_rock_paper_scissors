import unittest

from app.models.src.game import Game
from app.models.src.player import Player

class TestGame(unittest.TestCase):
    # def setUp(self):
        # self.player_1_name = "Bob"
        # self.player_2_name = "Tom"

    def test_draw__None(self):
        test_player_1 = Player("Bob", "Rock")
        test_player_2 = Player("Tom", "Rock")
        test_game = Game(test_player_1, test_player_2)
        self.assertEqual(None, test_game.play_game())

    def test_rock_paper__player2wins(self):
        test_player_1 = Player("Bob", "Rock")
        test_player_2 = Player("Tom", "Paper")
        test_game = Game(test_player_1, test_player_2)
        self.assertEqual("Tom wins by playing paper!", test_game.play_game())

    def test_rock_scissors__player1wins(self):
        test_player_1 = Player("Bob", "Rock")
        test_player_2 = Player("Tom", "Scissors")
        test_game = Game(test_player_1, test_player_2)
        self.assertEqual("Bob wins by playing rock!", test_game.play_game())

    def test_paper_rock__player1wins(self):
        test_player_1 = Player("Bob", "Paper")
        test_player_2 = Player("Tom", "Rock")
        test_game = Game(test_player_1, test_player_2)
        self.assertEqual("Bob wins by playing paper!", test_game.play_game())

    def test_paper_scissors__player2wins(self):
        test_player_1 = Player("Bob", "Paper")
        test_player_2 = Player("Tom", "Scissors")
        test_game = Game(test_player_1, test_player_2)
        self.assertEqual("Tom wins by playing scissors!", test_game.play_game())

    def test_scissors_rock__player2wins(self):
        test_player_1 = Player("Bob", "Scissors")
        test_player_2 = Player("Tom", "Rock")
        test_game = Game(test_player_1, test_player_2)
        self.assertEqual("Tom wins by playing rock!", test_game.play_game())

    def test_scissors_paper__player2wins(self):
        test_player_1 = Player("Bob", "Scissors")
        test_player_2 = Player("Tom", "Paper")
        test_game = Game(test_player_1, test_player_2)
        self.assertEqual("Bob wins by playing scissors!", test_game.play_game())