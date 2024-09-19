class BowlingGame:
    """
    A class to represent a bowling game and calculate the score based on rolls.
    """

    def __init__(self):
        """
        Initializes a new BowlingGame instance with an empty list of rolls.
        """
        self.rolls = []

    def roll(self, pins):
        """
        Records a roll in the game.
        
        Args:
            pins (int): The number of pins knocked down in the roll.
        """
        self.rolls.append(pins)

    def score(self):
        """
        Calculates the total score of the game based on the rolls.
        
        Returns:
            int: The total score of the game.
        """
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.calculateSpareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.calculateFrameScore(rollIndex)
                rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        """
        Determines if the roll at the given index is a strike.
        
        Args:
            rollIndex (int): The index of the current roll.
        
        Returns:
            bool: True if it's a strike, False otherwise.
        """
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        """
        Determines if the roll at the given index is a spare.
        
        Args:
            rollIndex (int): The index of the current roll.
        
        Returns:
            bool: True if it's a spare, False otherwise.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        """
        Calculates the score for a strike.
        
        Args:
            rollIndex (int): The index of the strike roll.
        
        Returns:
            int: The score for the strike frame.
        """
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def calculateSpareScore(self, rollIndex):
        """
        Calculates the score for a spare.
        
        Args:
            rollIndex (int): The index of the spare roll.
        
        Returns:
            int: The score for the spare frame.
        """
        return 10 + self.rolls[rollIndex + 2]

    def calculateFrameScore(self, rollIndex):
        """
        Calculates the score for a normal frame.
        
        Args:
            rollIndex (int): The index of the roll.
        
        Returns:
            int: The score for the normal frame.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
