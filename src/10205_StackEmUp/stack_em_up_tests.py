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

    def test_002(self):
        """get_card_name should return the expected name 002"""
        card = Card(1, 0)

        self.assertEqual("3 of Clubs", card.get_card_name())
        self.assertEqual(2, card.get_id())

    def test_003(self):
        """get_card_name should return the expected name 003"""
        card = Card(8, 0)

        self.assertEqual("10 of Clubs", card.get_card_name())
        self.assertEqual(9, card.get_id())

    def test_004(self):
        """get_card_name should return the expected name 004"""
        card = Card(9, 0)

        self.assertEqual("Jack of Clubs", card.get_card_name())
        self.assertEqual(10, card.get_id())
