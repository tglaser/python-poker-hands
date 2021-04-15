import unittest

from newsph.nsph import NewFancySimplePokerHands
from thirdparty.dealerservice import DealerService



class NewSimplePokerHandsTest(unittest.TestCase):


    def test_shouldReturnGivenCard_whenOnlyOneCardInHand(self):
        class DealerServiceForTest:
            def dealRandomHand(self):
                return ["H3"]

        sut = NewFancySimplePokerHands( DealerServiceForTest() )

        bestCard = sut.getBestCardFromDealedHand()

        self.assertEquals("H3", bestCard)
