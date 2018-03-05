__author__ = 'lene'

from argparse import ArgumentParser, Namespace

from compare_sets import jaccard_coefficient, similarity_matrix, recommendations
from read_file import read_file
from alternative_methods import asymmetric_similarity, minhash_similarity

from typing import Dict, List, Union
from typedefs import SimilarityFunction

SIMILARITY_FUNCTIONS: Dict[str, SimilarityFunction] = {
    'asymmetric_similarity': asymmetric_similarity,
    'minhash_similarity': minhash_similarity,
    'jaccard_coefficient': jaccard_coefficient
}


def parse() -> Namespace:
    parser = ArgumentParser(
        description="Give a set of recommended products for a user based on the user's liked "
                    "products and the products other users with similar taste liked."
    )
    parser.add_argument(
        '--filename', '-f', default='testdata.csv',
        help='File containing user IDs and their liked products (one per line, semicolon-separated)'
    )
    parser.add_argument(
        '--user', default='1', type=str,
        help='IDs (comma-separated) of the user(s) to receive recommendations'
    )
    parser.add_argument(
        '--set-comparison', default='jaccard_coefficient',
        help='Method used to compare two sets [{}]'.format('|'.join(SIMILARITY_FUNCTIONS.keys()))
    )
    parser.add_argument(
        '--cutoff', default=0.25, type=float,
        help='Value for similarity of liked products above which two users are considered similar'
    )

    return parser.parse_args()


args = parse()

set_comparison = SIMILARITY_FUNCTIONS[args.set_comparison]
liked_items = read_file(args.filename)
users: List[Union[int, str]] = [int(u) for u in args.user.split(',')]

similarity = similarity_matrix(liked_items, set_comparison, users)

for user in users:
    recommended = recommendations(user, liked_items, similarity, args.cutoff)
    print('User: {:>4d} Recommendations: {}'.format(user, recommended))
