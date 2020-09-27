from app.models.src.player import Player
from app.models.src.results import Results

class Game:
    def __init__(self, player_1, player_2):
        self.player_1_name = player_1.name.capitalize()
        self.choice_1 = player_1.choice.capitalize()
        self.player_2_name = player_2.name.capitalize()
        self.choice_2 = player_2.choice.capitalize()

    def play_game(self, results):
        if self.choice_1 == self.choice_2:
            results.result = "Draw"
            results.draws += 1
        elif self.choice_1 == "Rock":
            if self.choice_2 == "Paper":
                results.result = f"{self.player_2_name} wins by playing {self.choice_2.lower()}!"
                results.player_2_wins += 1
            elif self.choice_2 == "Scissors":
                results.result = f"{self.player_1_name} wins by playing {self.choice_1.lower()}!"
                results.player_1_wins += 1
        elif self.choice_1 == "Paper":
            if self.choice_2 == "Rock":
                results.result = f"{self.player_1_name} wins by playing {self.choice_1.lower()}!"
                results.player_1_wins += 1
            elif self.choice_2 == "Scissors":
                results.result = f"{self.player_2_name} wins by playing {self.choice_2.lower()}!"
                results.player_2_wins += 1
        elif self.choice_1 == "Scissors":
            if self.choice_2 == "Rock":
                results.result = f"{self.player_2_name} wins by playing {self.choice_2.lower()}!"
                results.player_2_wins += 1
            elif self.choice_2 == "Paper":
                results.result = f"{self.player_1_name} wins by playing {self.choice_1.lower()}!"
                results.player_1_wins += 1

