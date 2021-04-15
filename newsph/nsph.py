from tests.sph_test import SimplePokerHands
from thirdparty.dealerservice import DealerService


class NewFancySimplePokerHands:

    dealerService: DealerService

    def __init__(self, dealerService = DealerService() ):
        self.dealerService = dealerService

    def getBestCardFromDealedHand(self):
        hand = self.dealerService.dealRandomHand()
        return SimplePokerHands().bestFromHand(hand)
