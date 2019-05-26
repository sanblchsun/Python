print('Введите систему счисления')
base = int(input())
for num in range(1,11):
    print(num,'<=>',end='')
    while num>0:
        print(num%base,end='')
        num //= base
    print()