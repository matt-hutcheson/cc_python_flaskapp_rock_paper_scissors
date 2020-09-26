from src.player import Player

class Game:
    def __init__(self, player_1, player_2):
        self.player_1_name = player_1.name.capitalize()
        self.choice_1 = player_1.choice.capitalize()
        self.player_2_name = player_2.name.capitalize()
        self.choice_2 = player_2.choice.capitalize()

    def play_game(self, game_to_evaluate):
        choice_1 = game_to_evaluate.choice_1
        choice_2 = game_to_evaluate.choice_2
        player_1_name = game_to_evaluate.player_1_name
        player_2_name = game_to_evaluate.player_2_name
        if choice_1 == choice_2:
            return None
        elif choice_1 == "Rock":
            if choice_2 == "Paper":
                return f"{player_2_name} wins by playing {choice_2.lower()}!"
            elif choice_2 == "Scissors":
                return f"{player_1_name} wins by playing {choice_1.lower()}!"
        elif choice_1 == "Paper":
            if choice_2 == "Rock":
                return f"{player_1_name} wins by playing {choice_1.lower()}!"
            elif choice_2 == "Scissors":
                return f"{player_2_name} wins by playing {choice_2.lower()}!"
        elif choice_1 == "Scissors":
            if choice_2 == "Rock":
                return f"{player_2_name} wins by playing {choice_2.lower()}!"
            elif choice_2 == "Paper":
                return f"{player_1_name} wins by playing {choice_1.lower()}!"