"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    """A class to represent a bowling game and calculate scores."""

    def __init__(self):
        # Initialize a new game
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        """
        Record a roll.

        Args:
            pins (int): Number of pins knocked down

        Raises:
            ValueError: If pins are not between 0 and 10
        """
        if not isinstance(pins, int):
            raise ValueError("Pins must be an integer")

        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")

        # Prevent invalid frame totals (except strike)
        if len(self.rolls) % 2 == 1 and self.rolls[-1] != 10:
            if self.rolls[-1] + pins > 10:
                raise ValueError("Frame total cannot exceed 10")

        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        """
        Calculate total score for the bowling game.
        """
        score = 0
        frame_index = 0

        for frame in range(10):  # fixed: should be 10 frames
            if frame_index >= len(self.rolls):
                break

            if self._is_strike(frame_index):
                # Strike
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                # Spare
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                # Open frame
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
        bonus = 0
        if frame_index + 1 < len(self.rolls):
            bonus += self.rolls[frame_index + 1]
        if frame_index + 2 < len(self.rolls):
            bonus += self.rolls[frame_index + 2]
        return bonus

    def _spare_bonus(self, frame_index):
        if frame_index + 2 < len(self.rolls):
            return self.rolls[frame_index + 2]
        return 0

    def _sum_of_frame(self, frame_index):
        if frame_index + 1 < len(self.rolls):
            return self.rolls[frame_index] + self.rolls[frame_index + 1]
        return self.rolls[frame_index]