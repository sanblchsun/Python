print(1>2,1<2)
print(bool('spam'))
x = None
print(x)

l = [None] * 10
print(l)
print(type(type(l)))
if type(l) == type([]):
    print('yes')
if type(type(l)) == list:
    print('list')
elif type(type(l))==type:
    print('type')
if isinstance(l,list):
    print('ООП')