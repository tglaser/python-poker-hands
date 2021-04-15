import unittest

from newsph.nsph import NewFancySimplePokerHands


class NewSimplePokerHandsTest(unittest.TestCase):

    def test_initial_fail(self):
        sut = NewFancySimplePokerHands()
        self.fail("This is the inital test")
