a = [True] * 5 + [False] *5

print(type(a))
print(a)

for i in range(len(a)):
    print(i,'-','истина' if a[i] else 'ложь')