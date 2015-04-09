from compare_sets import jaccard_coefficient, similarity_matrix, similar_users, recommendations
from alternative_methods import asymmetric_similarity, minhash_similarity, minhashed
from read_file import read_file

__author__ = 'lene'

import unittest

class TestRecommender(unittest.TestCase):

    def test_jaccard(self):
        self.assertEqual(jaccard_coefficient({'a', 'b'}, {'b', 'a'}), 1.)
        self.assertEqual(jaccard_coefficient({'a', 'b'}, {'c', 'd'}), 0.)
        self.assertAlmostEqual(jaccard_coefficient({'a', 'b'}, {'a', 'c'}), 1./3.)

    def test_read_file(self):
        csv = read_file('testdata.csv')
        self.assertIsInstance(csv, dict)
        self.assertEqual(len(csv), 5)
        self.assertDictEqual(csv, { 1: {12, 99, 32}, 2: {32, 77, 54, 66}, 3: {99, 42, 12, 32}, 4: {77, 66, 47}, 5: {65}})

    def test_similarity_matrix_basic(self):
        self.assertDictEqual(
            similarity_matrix({ 1: {'a'}, 2: {'a'} }), { 1: { 1: 1.0, 2: 1.0 }, 2: { 1: 1.0, 2: 1.0 } }
        )
        self.assertDictEqual(
            similarity_matrix({ 1: {'a'}, 2: {'b'} }), { 1: { 1: 1.0, 2: 0.0 }, 2: { 1: 0.0, 2: 1.0 } }
        )

    def test_similarity_matrix_elements_equal_to_themselves(self):
        larger_list = { i: {i} for i in range(100) }
        larger_list_matrix = similarity_matrix(larger_list)
        self.assertEqual(len(larger_list_matrix), len(larger_list))
        for i in range(len(larger_list)):
            self.assertEqual(larger_list_matrix[i][i], 1.)


    def test_similarity_matrix_with_testdata(self):
        self.assertDictEqual(
            similarity_matrix(read_file('testdata.csv')), {
                1: {1: 1.0, 2: 0.16666666666666666, 3: 0.75, 4: 0.0, 5: 0.0},
                2: {1: 0.16666666666666666, 2: 1.0, 3: 0.14285714285714285, 4: 0.4, 5: 0.0},
                3: {1: 0.75, 2: 0.14285714285714285, 3: 1.0, 4: 0.0, 5: 0.0},
                4: {1: 0.0, 2: 0.4, 3: 0.0, 4: 1.0, 5: 0.0},
                5: {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 1.0}
            }
        )

    def test_similar_users(self):
        similarity = similarity_matrix({ 1: {'a'}, 2: {'a'} })
        self.assertEqual(similar_users(1, similarity, 0.2), [2])
        self.assertEqual(similar_users(2, similarity, 0.2), [1])
        self.assertEqual(similar_users(1, similarity, 1.0), [2])

        similarity = similarity_matrix({ 1: {'a'}, 2: {'b'} })
        self.assertEqual(similar_users(1, similarity, 0.2), [])

        similarity = similarity_matrix(read_file('testdata.csv'))
        self.assertEqual(similar_users(1, similarity, 0.2), [3])
        self.assertEqual(similar_users(2, similarity, 0.15), [1, 4])

    def test_recommendations(self):
        sets = { 1: {'a'}, 2: {'a', 'b'} }
        similarity = similarity_matrix(sets)
        self.assertEqual(recommendations(1, sets, similarity, 0.4), {'b'})
        self.assertEqual(recommendations(2, sets, similarity, 0.4), set())

    def test_recommendations_with_testdata(self):
        sets = read_file('testdata.csv')
        similarity = similarity_matrix(sets)
        self.assertEqual(recommendations(1, sets, similarity, 0.75), {42})
        self.assertFalse(recommendations(3, sets, similarity, 0.75))
        self.assertEqual(
            recommendations(1, sets, similarity, 0.15),
            (sets[2] | sets[3]) - sets[1]
        )

    def test_recommendations_with_zero_cutoff_returns_all_other_products(self):
        sets = read_file('testdata.csv')
        similarity = similarity_matrix(sets)
        for i in sets.keys():
            self.assertEqual(
                recommendations(i, sets, similarity, 0),
                reduce(lambda a, b: a | b, sets.values(), set()) - sets[i]
            )

    def test_asymmetric_similarity(self):
        self.assertEqual(asymmetric_similarity({'a'}, {'a', 'b'}), 1)
        self.assertEqual(asymmetric_similarity({'a', 'b'}, {'a'}), 0.5)
        sets = { 1: {'a'}, 2: {'a', 'b'} }
        similarity = similarity_matrix(sets, asymmetric_similarity)
        self.assertDictEqual(
            similarity, { 1: { 1: 1.0, 2: 1.0 }, 2: { 1: 0.5, 2: 1.0 } }
        )

    def test_asymmetric_similarity_returns_superset_of_jaccard(self):
        sets = read_file('testdata.csv')
        similarity1 = similarity_matrix(sets)
        similarity2 = similarity_matrix(sets, asymmetric_similarity)
        for i in sets.keys():
            self.assertTrue(
                recommendations(i, sets, similarity1, 0.25).issubset(recommendations(i, sets, similarity2, 0.25))
            )

    def test_minhash(self):
        self.assertEqual(minhashed({1}), {1})
        self.assertEqual(minhashed({1}, 2), {1})
        bigger_set = { i for i in range(100) }
        self.assertLessEqual(len(minhashed(bigger_set, 10)), 10)

    def test_minhash_similarity(self):
        self.assertEqual(minhash_similarity({1, 2}, {3, 4}), 0.)
        self.assertEqual(minhash_similarity({1, 2}, {2, 1}), 1.)

    def test_minhash_with_testdata(self):
        sets = read_file('testdata.csv')
        similarity = similarity_matrix(sets, minhash_similarity)
        self.assertEqual(recommendations(1, sets, similarity, 0.75), {42})
        self.assertFalse(recommendations(3, sets, similarity, 0.75))
        self.assertEqual(
            recommendations(1, sets, similarity, 0.15),
            (sets[2] | sets[3]) - sets[1]
        )

if __name__ == '__main__':
    unittest.main()
