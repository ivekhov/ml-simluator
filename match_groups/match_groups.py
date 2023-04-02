from typing import List
from typing import Tuple


test_data = [
	[
		[(1, 2), (7, 2)], 
		[(1, 2), (1, 7), (2, 7)]
	]
]


def extend_matches(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    #

    return pairs


def test(test_data, func):
	for item in test_data:
		assert func(item[0]) == item[-1]


def main():
    test(test_data, extend_matches)


if __name__ == '__main__':
	main()

