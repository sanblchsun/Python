import time

with open('mytest.txt') as f:
	for line in f:
		print(line, end=' ')
		time.sleep(2)