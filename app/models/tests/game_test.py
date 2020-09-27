import unittest

from app.models.src.game import Game
from app.models.src.player import Player
from app.models.src.results import Results

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Bob", "Rock")
        self.player_2 = Player("Tom", "Paper")
        self.test_results = Results()

    def test_draw__None(self):
        test_player_1 = Player("Bob", "Rock")
        test_player_2 = Player("Tom", "Rock")
        test_game = Game(test_player_1, test_player_2)
        draws = self.test_results.draws
        test_game.play_game(self.test_results)
        self.assertEqual(draws+1, self.test_results.draws)
        self.assertEqual("Draw", self.test_results.result)

    def test_rock_paper__player2wins(self):
        test_player_1 = Player("Bob", "Rock")
        test_player_2 = Player("Tom", "Paper")
        test_game = Game(test_player_1, test_player_2)
        p2wins = self.test_results.player_2_wins
        test_game.play_game(self.test_results)
        self.assertEqual(p2wins+1, self.test_results.player_2_wins)
        self.assertEqual("Tom wins by playing paper!", self.test_results.result)

    def test_rock_scissors__player1wins(self):
        test_player_1 = Player("Bob", "Rock")
        test_player_2 = Player("Tom", "Scissors")
        test_game = Game(test_player_1, test_player_2)
        p1wins = self.test_results.player_1_wins
        test_game.play_game(self.test_results)
        self.assertEqual(p1wins+1, self.test_results.player_1_wins)
        self.assertEqual("Bob wins by playing rock!", self.test_results.result)

    def test_paper_rock__player1wins(self):
        test_player_1 = Player("Bob", "Paper")
        test_player_2 = Player("Tom", "Rock")
        test_game = Game(test_player_1, test_player_2)
        p1wins = self.test_results.player_1_wins
        test_game.play_game(self.test_results)
        self.assertEqual(p1wins+1, self.test_results.player_1_wins)
        self.assertEqual("Bob wins by playing paper!", self.test_results.result)

    def test_paper_scissors__player2wins(self):
        test_player_1 = Player("Bob", "Paper")
        test_player_2 = Player("Tom", "Scissors")
        test_game = Game(test_player_1, test_player_2)
        p2wins = self.test_results.player_2_wins
        test_game.play_game(self.test_results)
        self.assertEqual(p2wins+1, self.test_results.player_2_wins)
        self.assertEqual("Tom wins by playing scissors!", self.test_results.result)

    def test_scissors_rock__player2wins(self):
        test_player_1 = Player("Bob", "Scissors")
        test_player_2 = Player("Tom", "Rock")
        test_game = Game(test_player_1, test_player_2)
        p2wins = self.test_results.player_2_wins
        test_game.play_game(self.test_results)
        self.assertEqual(p2wins+1, self.test_results.player_2_wins)
        self.assertEqual("Tom wins by playing rock!", self.test_results.result)

    def test_scissors_paper__player1wins(self):
        test_player_1 = Player("Bob", "Scissors")
        test_player_2 = Player("Tom", "Paper")
        test_game = Game(test_player_1, test_player_2)
        p1wins = self.test_results.player_1_wins
        test_game.play_game(self.test_results)
        self.assertEqual(p1wins+1, self.test_results.player_1_wins)
        self.assertEqual("Bob wins by playing scissors!", self.test_results.result)