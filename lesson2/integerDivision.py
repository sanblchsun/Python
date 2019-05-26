res = 1/3
print(res)
print(1//3.0)
print('%e' % res)
print('%4.2f' % res)
print('{0:4.2f}'.format(res))
print('----------------')
a = 2
b = 3
print(a,b)
a,b = b,a
print(a,b)
print('---------------')
for i in (1,2,3,4,5,6,7,8,9,10,11,12,22):
    print('-',i,'-')
    print('//:',-12//i,'%:',-12%i)
print('---------')
print(12/22,' ',12%22)
