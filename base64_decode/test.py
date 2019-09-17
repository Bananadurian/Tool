import itertools
import base64
import re
import sys

def delStr(str):
	p = itertools.product(('+', '/', '='), repeat = 2)
	for i in p:
		a = str.replace(" ", i[0], 1)
		a = a.replace(" ", i[1], 1)
		try:
			b = base64.b64decode(a)
			print(b.decode('utf-8'))
		except Exception as e:
			pass


def main():
	if len(sys.argv) == 2:
		try:
			path = sys.argv[1]
			str = ""
			with open(path, 'r') as f:
				str = f.read()
			delStr(str)
		except Exception as ret:
			print("请按照以下方式运行:")
			print("python3 test.py 文件名")


if __name__ == '__main__':
	main()