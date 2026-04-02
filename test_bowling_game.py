import unittest
from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    """Unit tests for BowlingGame."""

    def setUp(self):
        self.game = BowlingGame()

    def roll_many(self, n, pins):
        for _ in range(n):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        self.game.roll(10)

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_score_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(self.game.score(), 20)

    def test_one_spare(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(self.game.score(), 16)

    def test_one_strike(self):
        self.roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(self.game.score(), 24)

    def test_consecutive_strikes(self):
        self.roll_strike()
        self.roll_strike()
        self.game.roll(4)
        self.game.roll(2)
        self.roll_many(12, 0)
        self.assertEqual(self.game.score(), 46)

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(self.game.score(), 300)

    def test_all_spares(self):
        for _ in range(10):
            self.roll_spare()
        self.game.roll(5)
        self.assertEqual(self.game.score(), 150)

    def test_spare_in_last_frame(self):
        self.roll_many(18, 0)
        self.roll_spare()
        self.game.roll(7)
        self.assertEqual(self.game.score(), 17)

    def test_strike_in_last_frame(self):
        self.roll_many(18, 0)
        self.roll_strike()
        self.game.roll(3)
        self.game.roll(6)
        self.assertEqual(self.game.score(), 19)

    def test_invalid_negative(self):
        with self.assertRaises(ValueError):
            self.game.roll(-1)

    def test_invalid_too_high(self):
        with self.assertRaises(ValueError):
            self.game.roll(11)

    def test_frame_score_exceeds_ten(self):
        self.game.roll(8)
        with self.assertRaises(ValueError):
            self.game.roll(5)

    def test_too_many_rolls(self):
        """Ensure extra rolls do not crash the system."""
        self.roll_many(20, 0)
        self.game.roll(0)
        self.assertGreaterEqual(self.game.score(), 0)


if __name__ == "__main__":
    unittest.main()