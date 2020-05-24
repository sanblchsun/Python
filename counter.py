from collections import Counter

if (Counter('sSanblchsun') == Counter('nushcslbnaS')):
	print('Это анаграмма!')


mylist = [1,2,3,3,3,5,6,7,8,8]

data =  Counter(mylist)

print(data.most_common(3))