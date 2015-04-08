from compare_sets import jaccard_coefficient

__author__ = 'lene'

import unittest

class TestRecommender(unittest.TestCase):

    def test_jaccard(self):
        self.assertEqual(jaccard_coefficient({'a', 'b'}, {'b', 'a'}), 1.)
        self.assertEqual(jaccard_coefficient({'a', 'b'}, {'c', 'd'}), 0.)
        self.assertAlmostEqual(jaccard_coefficient({'a', 'b'}, {'a', 'c'}), 1./3.)

if __name__ == '__main__':
    unittest.main()
