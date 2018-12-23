import unittest

from stack_em_up import Card, Game


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

    def test_005(self):
        """get_card_name should return the expected name 005"""
        card = Card(10, 0)

        self.assertEqual("Queen of Clubs", card.get_card_name())
        self.assertEqual(11, card.get_id())

    def test_006(self):
        """get_card_name should return the expected name 005"""
        card = Card(11, 0)

        self.assertEqual("King of Clubs", card.get_card_name())
        self.assertEqual(12, card.get_id())

    def test_007(self):
        """get_card_name should return the expected name 007"""
        card = Card(12, 0)

        self.assertEqual("Ace of Clubs", card.get_card_name())
        self.assertEqual(13, card.get_id())

    def test_008(self):
        """get_card_name should error when given a value larger than 12"""

        def f():
            Card(13, 0)

        self.assertRaises(ValueError, f)

    def test_009(self):
        """get_card_name should return the expected name 009"""

        card = Card(0, 1)

        self.assertEqual("2 of Diamonds", card.get_card_name())
        self.assertEqual(14, card.get_id())

    def test_010(self):
        """get_card_name should return the expected name 009"""

        card = Card(1, 1)

        self.assertEqual("3 of Diamonds", card.get_card_name())
        self.assertEqual(15, card.get_id())

    def test_011(self):
        """get_card_name should return the expected name 010"""

        card = Card(8, 1)

        self.assertEqual("10 of Diamonds", card.get_card_name())
        self.assertEqual(22, card.get_id())

    def test_012(self):
        """get_card_name should return the expected name 010"""

        card = Card(9, 1)

        self.assertEqual("Jack of Diamonds", card.get_card_name())
        self.assertEqual(23, card.get_id())

    def test_013(self):
        """get_card_name should return the expected name 010"""

        card = Card(0, 2)

        self.assertEqual("2 of Hearts", card.get_card_name())
        self.assertEqual(27, card.get_id())

    def test_014(self):
        """get_card_name should error when given a suite greater than 3"""

        def f():
            Card(0, 4)

        self.assertRaises(ValueError, f)

    def test_015(self):
        """create_deck should return all 52 cards with expected ids"""

        deck = Game.create_deck()

        self.assertEqual(52, len(deck))

        for i in range(len(deck)):
            self.assertEqual(i + 1, deck[i].get_id())
