import unittest


class SimplePokerHands:
    def bestFromHand(self, handCards):
        return sorted(handCards, key=self.readNumericValue)[0]

    def readNumericValue(self, card):
        return card[1:]


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

    def test_shouldReturnK10_whenGivenTwoCardsInvertedOrderInvertedColors(self):
        sut = SimplePokerHands()

        bestCard = sut.bestFromHand(["K10", "C6"])

        self.assertEquals("K10", bestCard)

