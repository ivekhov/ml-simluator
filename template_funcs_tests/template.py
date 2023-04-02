from typing import List
from typing import Tuple


test_data = [
	[
		
		
	], 
	[
		
		
	]
]


def func():
    pass



def test(test_data, func):
	for item in test_data:
		assert func(item[0]) == item[-1]


def main():
    test(test_data, func)


if __name__ == '__main__':
	main()

