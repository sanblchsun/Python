rec = {'name': {'first': 'Bob', 'last': 'Smith'},'job': ['mgr'],'age': 'old'}

for k in sorted(rec): print(k, '=>', rec[k])

for ch in 'spam':
       print(ch.upper())
str = 'spam'
i = 0
print('-----------')
while i < len(str):
       print(str[i])
       i += 1
print(list(str))

sq = [x**2 for x in [1,2,3,4]]

print (sq)

rec['name']['firstnew'] = 'Jon'
print(rec)

print('name1' in rec)
print(rec.get('x',0))
print(rec['x'] if 'x' in rec else 0)
