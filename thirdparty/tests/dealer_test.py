import unittest

from thirdparty.dealerservice import DealerService


class DealerServiceTest(unittest.TestCase):

    def test_dealer_deals_random_hand(self):
        dealer: DealerService = DealerService()
        dealer._getTimeStamp = fakeTS1
        hand = dealer.dealRandomHand()

        self.assertListEqual(hand, ["H2", "PK", "PD", "C10", "H6"])

    def test_dealer_deals_random_hand_with_trailing_0_in_ts(self):
        dealer: DealerService = DealerService()
        dealer._getTimeStamp = fakeTS0
        hand = dealer.dealRandomHand()

        self.assertListEqual(hand, ["K3", "CD", "PK", "HA", "K10"])

    def test_dealer_deals_random_hand_with_trailing_9_in_ts(self):
        dealer: DealerService = DealerService()
        dealer._getTimeStamp = fakeTS9
        hand = dealer.dealRandomHand()

        self.assertListEqual(hand, ["C8", "K8", "C4", "P8", "H8"])

    def test_dealer_deals_real_random_hand(self):
        dealer: DealerService = DealerService()
        hand = dealer.dealRandomHand()

        self.assertEqual(len(hand), 5)


def fakeTS0() -> float:
    return 123456789.1230

def fakeTS1() -> float:
    return 123456789.1231

def fakeTS9() -> float:
    return 123456789.1239


