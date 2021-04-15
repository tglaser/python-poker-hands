import unittest


class SimplePokerHands:
    def bestFromHand(self, param):
        return sorted(param)[0]


class SimplePokerHandsTest(unittest.TestCase):

    def test_shouldReturnGivenCard_whenOnlyOneCardInHand(self):
        sut = SimplePokerHands()

        bestCard = sut.bestFromHand(["H3"])

        self.assertEquals("H3", bestCard)

    def test_shouldReturnHighest_whenGivenTwoCards(self):
        sut = SimplePokerHands()

        bestCard = sut.bestFromHand(["K6", "C10"])

        self.assertEquals("C10", bestCard)

    def test_shouldReturnHighest_whenGivenTwoCardsInvertedOrder(self):
        sut = SimplePokerHands()

        bestCard = sut.bestFromHand(["C10", "K6"])

        self.assertEquals("C10", bestCard)

