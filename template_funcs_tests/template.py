test_data = [
	[
		#
	], 
	[
		#
	]
]


def func():
    pass


def test(test_data, func):
	for item in test_data:
		try:
			assert func(item[0]) == item[-1]
		except:
			print('problem')
			print(item[0])
			print(func(item[0]))


def main():
    test(test_data, func)


if __name__ == '__main__':
	main()
