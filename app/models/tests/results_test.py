import unittest

from app.models.src.results import Results

class TestResults(unittest.TestCase):
    def setUp(self):
        self.test_start_results = Results()

    def test_results_exist(self):
        self.assertEqual(0, self.test_start_results.player_1_wins)
        self.assertEqual(0, self.test_start_results.draws)
        self.assertEqual(0, self.test_start_results.player_2_wins)
        self.assertEqual("result", self.test_start_results.result)
        self.assertEqual("Player 1", self.test_start_results.player_1_name)
        self.assertEqual("None", self.test_start_results.player_2_choice)
        self.assertEqual("Player 2", self.test_start_results.player_2_name)
        self.assertEqual("None", self.test_start_results.player_2_choice)
