__author__ = 'lene'

"""
Usage example:
>>> from read_file import read_file
>>> sets = read_file('testdata.csv')
>>> similarity = similarity_matrix(sets)
>>> user = 1
>>> cutoff = 0.25
>>> print(recommendations(user, sets, similarity, cutoff))
"""


def jaccard_coefficient(set1, set2):
    """
    A measure of similarity between two sets. Always between 0 (completely disjunct) and
    1 (containing the same elements).
    """
    return len(set1 & set2) / len(set1 | set2)


def similarity_matrix(sets, similarity=jaccard_coefficient):
    """
    :param sets:       Dict of sets, indexed by users. Similarity is computed between pairs of sets.
    :param similarity: Function to compute similarity between sets
    :return:           Dict of similarities between each pair of sets, indexed by user
    """
    return {
        user1: {
            user2: similarity(set1, set2) for (user2, set2) in sets.items()
        } for (user1, set1) in sets.items()
    }


def similar_users(user, similarity_matrix, cutoff):
    """
    :param user:                The user to find similar users for.
    :param similarity_matrix:   Matrix containing the similarity in taste to all other users.
    :param cutoff:              Similarity value above which users are considered similar.
    :return:                    List of users with similar taste to user.
    """
    return [
        other_user
        for other_user in similarity_matrix[user]
        if user != other_user and similarity_matrix[user][other_user] >= cutoff
    ]


def recommendations(user, sets, similarity_matrix, cutoff):
    """
    :param sets:    All users and their liked products.
    :return:        Recommended products for user based on the products similar users liked.
    """
    return {
        item
        for similar in similar_users(user, similarity_matrix, cutoff)
        for item in sets[similar] - sets[user]
    }
