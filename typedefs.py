__author__ = 'Lene Preuss <lene.preuss@gmail.com>'

from typing import Set, Union, Dict, Callable, Any

User = Union[int, str]
Item = Any
LikedItems = Dict[User, Set[Item]]
SimilarityFunction = Callable[[Set, Set], float]
SimilarityMatrix = Dict[User, Dict[User, float]]
