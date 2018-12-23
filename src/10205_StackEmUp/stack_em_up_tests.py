import unittest

from stack_em_up import Card


class StackEmUpTests(unittest.TestCase):
    pass


class CardTypeTests(unittest.TestCase):
    def test_001(self):
        """get_card_name should return the expected name 001"""
        card = Card(0, 0)

        self.assertEqual("2 of Clubs", card.get_card_name())
        self.assertEqual(1, card.get_id())
