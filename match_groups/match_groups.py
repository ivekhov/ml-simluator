from typing import List
from typing import Tuple


test_data = [
	[
		[(1, 2), (7, 2)], 
		[(1, 2), (1, 7), (2, 7)]
	], 
	[
		[], 
		[]
	], 
	[
		[(1, 4), (2, 3)],
		[(1, 4), (2, 3)]
	],
	[
		[(2, 3), (1, 4)],
		[(1, 4), (2, 3)]
	],
	
	[
		[(1, 2), (1, 2)],
		[(1, 2)]
	], 
	[
		[(1, 2), (2, 3), (5, 3), (4, 6), (6, 7), (8, 9), (1, 3), (2, 5), (4, 7)], 
		[(1, 2), (1, 3), (1, 5), (2, 3), (2, 5), (3, 5), (4, 6), (4, 7), (6, 7), (8, 9)]
	],
	[
		[(1, 2), (2, 3), (3, 4)],
		[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
	],
	[
		[(1, 2), (2, 3), (5, 3), (4, 6), (6, 7), (8, 9)], 
		[(1, 2), (1, 3), (1, 5), (2, 3), (2, 5), (3, 5), (4, 6), (4, 7), (6, 7), (8, 9)]
	]
]


def extend_matches(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
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
			
			# for match in result:
			# 	if len(set(pair).intersection(set(match))) == 1:
			# 		result.add(tuple(pair))
			# 		result.add(tuple(match))
			# 		result.add(tuple(set(pair).union(set(match)).difference(set(pair).intersection(set(match)))))

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
			print(item[0])
			print(func(item[0]))


def main():
    test(test_data, extend_matches)


if __name__ == '__main__':
	main()
