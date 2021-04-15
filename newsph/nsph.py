from thirdparty.dealerservice import DealerService


class NewFancySimplePokerHands:

    def getBestCardFromDealedHand(self):
        hand = DealerService().dealRandomHand()
        return hand[-1]
