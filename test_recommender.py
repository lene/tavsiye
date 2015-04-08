from compare_sets import jaccard_coefficient, naive_comparison
from read_file import read_file

__author__ = 'lene'

import unittest

class TestRecommender(unittest.TestCase):

    def test_jaccard(self):
        self.assertEqual(jaccard_coefficient({'a', 'b'}, {'b', 'a'}), 1.)
        self.assertEqual(jaccard_coefficient({'a', 'b'}, {'c', 'd'}), 0.)
        self.assertAlmostEqual(jaccard_coefficient({'a', 'b'}, {'a', 'c'}), 1./3.)

    def test_naive_comparison_trivial(self):
        self.assertEqual(naive_comparison([{'a'}]), [[1.]])
        self.assertEqual(naive_comparison([{'a'}, {'a'}]), [[1., 1.], [1., 1.]])

    def test_naive_comparison_larger(self):
        self.assertEqual(naive_comparison([{'a', 'b'}, {'b', 'a'}]), [[1., 1.], [1., 1.]])
        self.assertEqual(
            naive_comparison([{'a', 'b'}, {'b', 'a'}, {'c', 'd'}]),
            [[1., 1., 0.], [1., 1., 0], [0., 0., 1.]]
        )

    def test_naive_comparison_different_sizes(self):
        self.assertEqual(naive_comparison([{'a', 'b'}, {'a'}]), [[1., 0.5], [0.5, 1.]])

    def test_read_file(self):
        csv = read_file('testdata.csv')
        self.assertIsInstance(csv, dict)
        self.assertEqual(len(csv), 5)
        self.assertDictEqual(csv, { 1: {12, 99, 32}, 2: {32, 77, 54, 66}, 3: {99, 42, 12, 32}, 4: {77, 66, 47}, 5: {65}})

if __name__ == '__main__':
    unittest.main()
