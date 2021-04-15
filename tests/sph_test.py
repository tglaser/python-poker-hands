import unittest

from typing import Dict

class SimplePokerHands:

    pictures : Dict[str,int] = { "B" : 11,
                                 "D" : 12,
                                 "K" : 13,
                                 "A" : 14 }

    def bestFromHand(self, handCards):
        return sorted(handCards, key=self.readNumericValue)[-1]

    def readNumericValue(self, card):
        if card[-1] in self.pictures:
            return self.pictures.get(card[-1])
        return int(card[1:])


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

    def test_shouldReturnK10_whenGivenFiveCards(self):
        sut = SimplePokerHands()

        bestCard = sut.bestFromHand(["C6", "K10", "C2", "C8", "H7"])

        self.assertEquals("K10", bestCard)

    def test_shouldReturnHB_whenGivenFiveCardsWithJacks(self):
        sut = SimplePokerHands()

        bestCard = sut.bestFromHand(["C6", "K10", "C2", "HB", "H7"])

        self.assertEquals("HB", bestCard)

    def test_shouldReturnPD_whenGivenFiveCardsWithPictures(self):
        sut = SimplePokerHands()

        bestCard = sut.bestFromHand(["C6", "K10", "PD", "HB", "H7"])

        self.assertEquals("PD", bestCard)

    def test_shouldReturnKA_whenGivenFiveCardsWithPictures(self):
        sut = SimplePokerHands()

        bestCard = sut.bestFromHand(["C6", "K10", "PD", "KK", "KA"])

        self.assertEquals("KA", bestCard)
