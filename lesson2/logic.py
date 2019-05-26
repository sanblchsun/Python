print('введите целое число')
n = int(input())
for i in range(n):
    print(i,(i%2==0) & (i%3==0))
