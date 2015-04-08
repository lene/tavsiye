from compare_sets import jaccard_coefficient, naive_comparison, comparison_with_dict, similar_users
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

    def test_naive_comparison_elements_equal_to_themselves(self):
        larger_list = [ {i} for i in range(100) ]
        larger_list_matrix = naive_comparison(larger_list)
        self.assertEqual(len(larger_list_matrix), len(larger_list))
        for i in range(len(larger_list)):
            self.assertEqual(larger_list_matrix[i][i], 1.)

    def test_read_file(self):
        csv = read_file('testdata.csv')
        self.assertIsInstance(csv, dict)
        self.assertEqual(len(csv), 5)
        self.assertDictEqual(csv, { 1: {12, 99, 32}, 2: {32, 77, 54, 66}, 3: {99, 42, 12, 32}, 4: {77, 66, 47}, 5: {65}})

    def test_comparison_with_dicts(self):
        self.assertDictEqual(
            comparison_with_dict({ 1: {'a'}, 2: {'a'} }), { 1: { 1: 1.0, 2: 1.0 }, 2: { 1: 1.0, 2: 1.0 } }
        )
        self.assertDictEqual(
            comparison_with_dict({ 1: {'a'}, 2: {'b'} }), { 1: { 1: 1.0, 2: 0.0 }, 2: { 1: 0.0, 2: 1.0 } }
        )

    def test_comparison_with_testdata(self):
        self.assertDictEqual(
            comparison_with_dict(read_file('testdata.csv')), {
                1: {1: 1.0, 2: 0.16666666666666666, 3: 0.75, 4: 0.0, 5: 0.0},
                2: {1: 0.16666666666666666, 2: 1.0, 3: 0.14285714285714285, 4: 0.4, 5: 0.0},
                3: {1: 0.75, 2: 0.14285714285714285, 3: 1.0, 4: 0.0, 5: 0.0},
                4: {1: 0.0, 2: 0.4, 3: 0.0, 4: 1.0, 5: 0.0},
                5: {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 1.0}
            }
        )

    def test_similar_users(self):
        similarity = comparison_with_dict({ 1: {'a'}, 2: {'a'} })
        self.assertEqual(similar_users(1, similarity, 0.2), [2])
        self.assertEqual(similar_users(2, similarity, 0.2), [1])
        self.assertEqual(similar_users(1, similarity, 1.0), [2])

        similarity = comparison_with_dict({ 1: {'a'}, 2: {'b'} })
        self.assertEqual(similar_users(1, similarity, 0.2), [])

        similarity = comparison_with_dict(read_file('testdata.csv'))
        self.assertEqual(similar_users(1, similarity, 0.2), [3])
        self.assertEqual(similar_users(2, similarity, 0.15), [1, 4])

if __name__ == '__main__':
    unittest.main()
