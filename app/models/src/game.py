from app.models.src.player import Player

results = {
    "Player 1 wins":0,
    "draws":0,
    "Player 2 wins":0,
    "Result":"play game"
}

class Game:
    def __init__(self, player_1, player_2):
        self.player_1_name = player_1.name.capitalize()
        self.choice_1 = player_1.choice.capitalize()
        self.player_2_name = player_2.name.capitalize()
        self.choice_2 = player_2.choice.capitalize()

    def play_game(self):
        if self.choice_1 == self.choice_2:
            result["Result"] = "Draw"
            results["draws"] += 1
        elif self.choice_1 == "Rock":
            if self.choice_2 == "Paper":
                results["Result"] = f"{self.player_2_name} wins by playing {self.choice_2.lower()}!"
                results["Player 2 wins"] += 1
            elif self.choice_2 == "Scissors":
                results["Result"] = f"{self.player_1_name} wins by playing {self.choice_1.lower()}!"
                results["Player 1 wins"] += 1
        elif self.choice_1 == "Paper":
            if self.choice_2 == "Rock":
                results["Result"] = f"{self.player_1_name} wins by playing {self.choice_1.lower()}!"
                results["Player 1 wins"] += 1
            elif self.choice_2 == "Scissors":
                results["Result"] = f"{self.player_2_name} wins by playing {self.choice_2.lower()}!"
                results["Player 2 wins"] += 1
        elif self.choice_1 == "Scissors":
            if self.choice_2 == "Rock":
                results["Result"] = f"{self.player_2_name} wins by playing {self.choice_2.lower()}!"
                results["Player 2 wins"] += 1
            elif self.choice_2 == "Paper":
                results["Result"] = f"{self.player_1_name} wins by playing {self.choice_1.lower()}!"
                results["Player 1 wins"] += 1

