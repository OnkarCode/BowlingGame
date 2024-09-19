import unittest
import BowlingGame

# Test class for simple cases (Gutter and All Ones)
class TestSimpleCases(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        self.rollMany(0, 20)
        self.assertEqual(self.game.score(), 0)

    def testAllOnes(self):
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20)

    def rollMany(self, pins, rolls):
        for _ in range(rolls):
            self.game.roll(pins)

# Test class for bonuses (Spare and Strike)
class TestBonusCases(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(self.game.score(), 16)

    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24)

    def rollMany(self, pins, rolls):
        for _ in range(rolls):
            self.game.roll(pins)

# Test class for Perfect Game
class TestPerfectGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testPerfectGame(self):
        self.rollMany(10, 12)
        self.assertEqual(self.game.score(), 300)

    def rollMany(self, pins, rolls):
        for _ in range(rolls):
            self.game.roll(pins)

# Entry point to run all tests
if __name__ == "__main__":
    unittest.main()