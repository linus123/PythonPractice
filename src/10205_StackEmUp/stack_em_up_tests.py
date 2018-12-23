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

    def test_016(self):
        game = Game()
        game.add_shuffle([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 51])
        game.add_shuffle([52, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 1])

        game.apply_shuffle(1)
        game.apply_shuffle(2)

        deck = list(game.get_current_deck())

        self.assertEqual("King of Spades", deck[0])
        self.assertEqual("2 of Clubs", deck[1])
        self.assertEqual("4 of Clubs", deck[2])
        self.assertEqual("5 of Clubs", deck[3])
        self.assertEqual("6 of Clubs", deck[4])
        self.assertEqual("7 of Clubs", deck[5])
        self.assertEqual("8 of Clubs", deck[6])
        self.assertEqual("9 of Clubs", deck[7])
        self.assertEqual("10 of Clubs", deck[8])
        self.assertEqual("Jack of Clubs", deck[9])
        self.assertEqual("Queen of Clubs", deck[10])
        self.assertEqual("King of Clubs", deck[11])
        self.assertEqual("Ace of Clubs", deck[12])
        self.assertEqual("2 of Diamonds", deck[13])
        self.assertEqual("3 of Diamonds", deck[14])
        self.assertEqual("4 of Diamonds", deck[15])
        self.assertEqual("5 of Diamonds", deck[16])
        self.assertEqual("6 of Diamonds", deck[17])
        self.assertEqual("7 of Diamonds", deck[18])
        self.assertEqual("8 of Diamonds", deck[19])
        self.assertEqual("9 of Diamonds", deck[20])
        self.assertEqual("10 of Diamonds", deck[21])
        self.assertEqual("Jack of Diamonds", deck[22])
        self.assertEqual("Queen of Diamonds", deck[23])
        self.assertEqual("King of Diamonds", deck[24])
        self.assertEqual("Ace of Diamonds", deck[25])
        self.assertEqual("2 of Hearts", deck[26])
        self.assertEqual("3 of Hearts", deck[27])
        self.assertEqual("4 of Hearts", deck[28])
        self.assertEqual("5 of Hearts", deck[29])
        self.assertEqual("6 of Hearts", deck[30])
        self.assertEqual("7 of Hearts", deck[31])
        self.assertEqual("8 of Hearts", deck[32])
        self.assertEqual("9 of Hearts", deck[33])
        self.assertEqual("10 of Hearts", deck[34])
        self.assertEqual("Jack of Hearts", deck[35])
        self.assertEqual("Queen of Hearts", deck[36])
        self.assertEqual("King of Hearts", deck[37])
        self.assertEqual("Ace of Hearts", deck[38])
        self.assertEqual("2 of Spades", deck[39])
        self.assertEqual("3 of Spades", deck[40])
        self.assertEqual("4 of Spades", deck[41])
        self.assertEqual("5 of Spades", deck[42])
        self.assertEqual("6 of Spades", deck[43])
        self.assertEqual("7 of Spades", deck[44])
        self.assertEqual("8 of Spades", deck[45])
        self.assertEqual("9 of Spades", deck[46])
        self.assertEqual("10 of Spades", deck[47])
        self.assertEqual("Jack of Spades", deck[48])
        self.assertEqual("Queen of Spades", deck[49])
        self.assertEqual("Ace of Spades", deck[50])
        self.assertEqual("3 of Clubs", deck[51])

