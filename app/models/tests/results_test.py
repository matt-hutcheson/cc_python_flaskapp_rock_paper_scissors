import unittest

from app.models.src.results import Results

class TestResults(unittest.TestCase):
    def setUp(self):
        self.test_start_results = Results(0,0,0,"play game")
        self.test_game_results = Results(4,2,6,"Bob wins by playing Paper!")

    def test_results_exist(self):
        self.assertEqual(0, self.test_start_results.player_1_wins)
        self.assertEqual(0, self.test_start_results.draws)
        self.assertEqual(0, self.test_start_results.player_2_wins)
        self.assertEqual("play game", self.test_start_results.result)

    def test_game_results_exist(self):
        self.assertEqual(4, self.test_game_results.player_1_wins)
        self.assertEqual(2, self.test_game_results.draws)
        self.assertEqual(6, self.test_game_results.player_2_wins)
        self.assertEqual("Bob wins by playing Paper!", self.test_game_results.result)