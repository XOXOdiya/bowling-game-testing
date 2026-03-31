"""
Bowling Game Implementation
Handles scoring for a standard 10-pin bowling game.
"""

class BowlingGame:
    """
    Represents a bowling game and calculates score based on bowling rules.
    """

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        """
        Record a roll.

        Args:
            pins (int): pins knocked down (0–10)

        Raises:
            ValueError: if pins are invalid
        """
        if not isinstance(pins, int):
            raise ValueError("Pins must be an integer")

        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")

        self.rolls.append(pins)

    def score(self):
        """
        Calculate total score for the game.

        Returns:
            int: final bowling score
        """
        score = 0
        frame_index = 0

        for _ in range(10):  # 10 frames
            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self._sum_of_frame(frame_index)
                frame_index += 2

        return score



    def _is_strike(self, frame_index):
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        return (
            frame_index + 1 < len(self.rolls)
            and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10
        )

    def _strike_bonus(self, frame_index):
        if frame_index + 2 < len(self.rolls):
            return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
        return 0

    def _spare_bonus(self, frame_index):
        if frame_index + 2 < len(self.rolls):
            return self.rolls[frame_index + 2]
        return 0

    def _sum_of_frame(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]