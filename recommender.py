__author__ = 'lene'

from argparse import ArgumentParser

from compare_sets import jaccard_coefficient, similarity_matrix, recommendations
from read_file import read_file
from alternative_methods import asymmetric_similarity, minhash_similarity

parser = ArgumentParser(description="Give a set of recommended products for a user based on the user's liked products and the products other users with similar taste liked.")
parser.add_argument(
    '--filename', '-f', default='testdata.csv',
    help='File containing user IDs and their liked products (one per line, semicolon-separated)'
)
parser.add_argument(
    '--user', default=1, type=int,
    help='ID of the user to receive recommendations'
)
parser.add_argument(
    '--set-comparison', default='jaccard_coefficient',
    help='Method used to compare two sets [jaccard_coefficient|asymmetric_similarity|minhash_similarity]'
)
parser.add_argument(
    '--cutoff', default=0.25, type=float,
    help='Value for similarity of liked products above which two users are considered similar'
)

args = parser.parse_args()
if args.set_comparison == 'asymmetric_similarity':
    set_comparison = asymmetric_similarity
elif args.set_comparison == 'minhash_similarity':
    set_comparison = minhash_similarity
else:
    set_comparison = jaccard_coefficient

sets = read_file(args.filename)
similarity = similarity_matrix(sets, set_comparison)
recommended = recommendations(args.user, sets, similarity, args.cutoff)

print(recommended)