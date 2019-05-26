a = [1] * 5 + [3] *5
x = 10
print(a)
a.append(x)
print(a)
print(a.pop())
a.insert(3,-10)
print(a)
a.remove(1)
print(a)

b = [x**2 for x in range(10)]
print(b)
c = []
for x in b: print(x)
for x in b:
    if x%2==0: c.append(x)

print(c)
c.clear()
print(c)
print('-------')
c = [x for x in b if x%2==0 or x==49]
print(c)

