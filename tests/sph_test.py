import unittest


class SimplePokerHands:
    def bestFromHand(self, param):
        return param[0]


class SimplePokerHandsTest(unittest.TestCase):

    def test_shouldReturnGivenCard_whenOnlyOneCardInHand(self):
        sut = SimplePokerHands()

        bestCard = sut.bestFromHand(["H3"])

        self.assertEquals("H3", bestCard)
