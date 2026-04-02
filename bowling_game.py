"""
Bowling Game Implementation
Handles scoring for a standard 10-pin bowling game.
"""


class BowlingGame:
    """bowling game and calculates score."""

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        """Record a roll."""
        if not isinstance(pins, int):
            raise ValueError("Pins must be an integer")

        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")

        # Prevent invalid frame totals (except strike)
        if len(self.rolls) % 2 == 1 and self.rolls[-1] != 10:
            if self.rolls[-1] + pins > 10:
                raise ValueError("Frame total cannot exceed 10")

        self.rolls.append(pins)

    def score(self):
        """Calculate total score."""
        score = 0
        frame_index = 0

        for _ in range(10):
            if frame_index >= len(self.rolls):
                break

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

    def _is_strike(self, i):
        return i < len(self.rolls) and self.rolls[i] == 10

    def _is_spare(self, i):
        return (
            i + 1 < len(self.rolls)
            and self.rolls[i] + self.rolls[i + 1] == 10
        )

    def _strike_bonus(self, i):
        bonus = 0
        if i + 1 < len(self.rolls):
            bonus += self.rolls[i + 1]
        if i + 2 < len(self.rolls):
            bonus += self.rolls[i + 2]
        return bonus

    def _spare_bonus(self, i):
        if i + 2 < len(self.rolls):
            return self.rolls[i + 2]
        return 0

    def _sum_of_frame(self, i):
        if i + 1 < len(self.rolls):
            return self.rolls[i] + self.rolls[i + 1]
        return self.rolls[i]