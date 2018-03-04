A very basic recommendation engine implemented in Python.

Usage:
    `python recommender.py [-h|-f FILENAME|--user USER|--set-comparison SET_COMPARISON|--cutoff CUTOFF]`

Running test suite:
    `python test_recommender.py && mypy . && flake8 --max-line-length=100`

Implementation thoughts:
- The entire recommendation algorithm can be found in compare_sets.py.
- I found it useful to plug different algorithms for computing the similarity of sets into the
 recommendation engine. The other comparison algorithms can be found in alternative_methods.py.
- In principle, nothing stops you from plugging custom objects as a similarity_matrix into
 the similar_users() and recommendations() functions. (I don't supply an example for this though.)
 You might want to do that because the similarity_matrix I calculate grows is O(N^2) in the number
 of users - in real world settings you'd want to optimize this.
- You have to decide on a numeric value for the similarity of two sets of liked products to
 consider two users similar in taste. I plugged that value as parameter 'cutoff' into the relevant
 functions.
- I am not sure the MinHash-algorithm I used is stable - I sort of whipped it up. It is hard to
 test stochastic algorithms, I considered this outside the scope of this exercise.
