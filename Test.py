import unittest
import BowlingGame

class TestSimpleCases(unittest.TestCase):
    """
    Test cases for simple bowling games (Gutter game and All Ones).
    """

    def setUp(self):
        """
        Set up a new BowlingGame instance before each test.
        """
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        """
        Test a gutter game where no pins are knocked down.
        """
        self.rollMany(0, 20)
        self.assertEqual(self.game.score(), 0)

    def testAllOnes(self):
        """
        Test a game where the player hits 1 pin in each roll.
        """
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20)

    def rollMany(self, pins, rolls):
        """
        Helper method to roll multiple times in a game.
        
        Args:
            pins (int): The number of pins knocked down in each roll.
            rolls (int): The number of rolls to perform.
        """
        for _ in range(rolls):
            self.game.roll(pins)

class TestBonusCases(unittest.TestCase):
    """
    Test cases for scoring bonuses (Spare and Strike).
    """

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testOneSpare(self):
        """
        Test a game with one spare and subsequent rolls.
        """
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(self.game.score(), 16)

    def testOneStrike(self):
        """
        Test a game with one strike and subsequent rolls.
        """
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24)

    def rollMany(self, pins, rolls):
        for _ in range(rolls):
            self.game.roll(pins)

class TestPerfectGame(unittest.TestCase):
    """
    Test case for a perfect game (12 strikes).
    """

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testPerfectGame(self):
        """
        Test a perfect game where all rolls are strikes.
        """
        self.rollMany(10, 12)
        self.assertEqual(self.game.score(), 300)

    def rollMany(self, pins, rolls):
        for _ in range(rolls):
            self.game.roll(pins)

if __name__ == "__main__":
    unittest.main()
