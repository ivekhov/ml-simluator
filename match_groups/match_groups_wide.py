"""Solution of matching groups with sets types."""
from collections import defaultdict
from typing import List
from typing import Tuple


data = [
    [
        [(5, 3, 4, 8), (1, 2), (7, 2)],
        [(1, 2, 7), (3, 4, 5, 8)]
    ],
    [
        [(1, 2), (2, 3), (3, 4)],
        [(1, 2, 3, 4)]
    ],
    [
        [(1, 2), (2, 3), (5, 3), (4, 6), (6, 7), (8, 9)],
        [(1, 2, 3, 5), (4, 6, 7), (8, 9)],
    ],
]


def extend_matches(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    storage = defaultdict(lambda: set())
    unique_nums = set()
    for pair in pairs:
        unique_nums |= set(pair)
    for pair in pairs:
        for num in pair:
            storage[num] |= set(pair)

    combinations = set()
    for items in storage.values():
        temp_union = set()
        for item in items:
            temp_union |= storage[item]
            for group in combinations.copy():
                if set(group) <= temp_union:
                    combinations.remove(group)
                if set(group) >= temp_union:
                    temp_union |= set(group)
            combinations.add(tuple(sorted(temp_union)))

    return sorted(list(combinations))
