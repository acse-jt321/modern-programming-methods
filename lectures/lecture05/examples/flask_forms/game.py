import random


class PaperScissorsStone:
    """Class implementing a game (with memory)."""

    _results = ["It's a draw.", "I win!", 'You win!']

    def __init__(self, score=None):
        self.score = score or [0, 0]

    def play_round(self, player_choice):
        """Play one round of Paper, Scissors, Stone, aka
        Rock paper scissors."""

        my_choice = random.randrange(0, 3)
        result = (my_choice-player_choice) % 3

        if result == 2:
            self.score[0] += 1
        elif result == 1:
            self.score[1] += 1

        return self._results[result], my_choice

    def reset(self):
        """Reset the score counter to zero."""
        self.score = [0, 0]
