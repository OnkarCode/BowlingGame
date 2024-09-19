class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        rollIndex = 0

        # Loop through each frame (10 frames)
        for frameIndex in range(10):
            if self.isStrike(rollIndex):  # Strike case
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):  # Spare case
                result += self.calculateSpareScore(rollIndex)
                rollIndex += 2
            else:  # Regular frame
                result += self.calculateFrameScore(rollIndex)
                rollIndex += 2

        return result

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def calculateSpareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]

    def calculateFrameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
