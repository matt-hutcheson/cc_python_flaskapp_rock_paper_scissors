class Results():
    def __init__(self):
        self.player_1_wins = 0
        self.player_2_wins = 0
        self.draws = 0
        self.result = "result"
        self.player_1_name = "Player 1"
        self.player_2_name = "Player 2"
        self.player_1_choice = "None"
        self.player_2_choice = "None"
        self.ai_check = False

    def reset_scores(self):
        self.player_1_wins = 0
        self.player_2_wins = 0
        self.draws = 0
        self.result = "result"
        self.player_1_name = "Player 1"
        self.player_1_choice = "None"
        self.player_2_name = "Player 2"
        self.player_2_choice = "None"