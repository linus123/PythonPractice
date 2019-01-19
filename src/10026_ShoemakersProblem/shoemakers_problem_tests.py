import unittest

from shoemakers_problem import *


class ShoemakersProblemTests(unittest.TestCase):
    def test_000(self):
        """Should return the single item given a single item"""

        job1 = ShoeJob(3, 4)

        results = get_best_order([job1])

        self.assertEqual([1], results)
        
    def test_001(self):
        """Should return the larger find given two items"""
        
        job1 = ShoeJob(3, 0)
        job2 = ShoeJob(5, 5)

        results = get_best_order([job1, job2])

        self.assertEqual([2, 1], results)

    def test_002(self):
        """Should return time when largest time first is not always the smallest cost"""

        job1 = ShoeJob(3, 4)
        job2 = ShoeJob(2, 2)
        job3 = ShoeJob(5, 5)

        results = get_best_order([job1, job2, job3])

        print(get_cost([job3, job1, job2]))
        print(get_cost([job1, job2, job3]))

        self.assertEqual([1, 2, 3], results)

    def test_100(self):
        """get_cost should return correct value"""
        job1 = ShoeJob(3, 4)

        cost = get_cost([job1])

        self.assertEqual(0, cost)

    def test_101(self):
        """get_cost should return correct value"""
        job1 = ShoeJob(1, 4)
        job2 = ShoeJob(10, 3)

        cost = get_cost([job1, job2])

        self.assertEqual(3, cost)

    def test_102(self):
        """get_cost should return correct value for more that two waiting jobs"""
        job1 = ShoeJob(1, 10)
        job1.order = 1

        job2 = ShoeJob(1, 10)
        job2.order = 2

        job3 = ShoeJob(1, 10)
        job3.order = 3

        cost = get_cost([job1, job2, job3])

        self.assertEqual(20 + 10, cost)

    def test_103(self):
        """get_cost should return correct value for more that two waiting jobs"""
        job1 = ShoeJob(1, 10)
        job1.order = 1

        job2 = ShoeJob(2, 10)
        job2.order = 2

        job3 = ShoeJob(3, 10)
        job3.order = 3

        cost = get_cost([job1, job2, job3])

        self.assertEqual(20 + 20, cost)

    def test_500(self):
        """Sample problem should work"""

        job1 = ShoeJob(3, 4)
        job2 = ShoeJob(1, 1000)
        job3 = ShoeJob(2, 2)
        job4 = ShoeJob(5, 5)

        results = get_best_order([job1, job2, job3, job4])

        self.assertEqual([2, 1, 3, 4], results)

