from collections import defaultdict
from itertools import permutations
from typing import List
from typing import Tuple


test_data = [
    [
        [(5, 3, 4, 8), (1, 2), (7, 2)],
        [(1, 2, 7), (3, 4, 5, 8)]
    ],
]


def init_dict():
    return set()


def extend_matches(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    storage = defaultdict(init_dict)
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
            combinations.add(tuple(sorted(temp_union)))

    return sorted(list(combinations))


def __extend_matches(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if len(pairs) == 0:
        return []
    items = pairs.copy()
    result = set()
    while len(items) != 0:
        pair = items.pop()
        for item in items:
            if pair == item:
                result.add(pair)
                continue
            if len(set(pair).intersection(set(item))) == 1:
                result.add(tuple(pair))
                result.add(tuple(item))
                result.add(tuple(set(pair).union(set(item)).difference(set(pair).intersection(set(item)))))

    unique_pairs = list(tuple(set(pairs).difference(set(result))))
    for pair in unique_pairs:
        result.add(pair)

    new_arr = set([tuple(set(item)) for item in result])

    return sorted(list(new_arr))


def test(test_data, func):
    for item in test_data:
        try:
            assert func(item[0]) == item[-1]
            # print(item[0])
            # print(func(item[0]))
        except:
            print('problem')
            # print(item[0])
            print(func(item[0]))


def main():
    test(test_data, extend_matches)


if __name__ == '__main__':
    main()
