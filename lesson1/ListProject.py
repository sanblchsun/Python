lst1 = [1,2,3]
lst2 = [x**2 for x in range(10) if x%2==1]
lst3 = list("abcde")
print(lst1,lst2,lst3)

print(lst2[0],lst2[-1],lst2[2])

lst2[2] = -2
print(lst2)

del lst2[2]
print(lst2)
print("--------")
s = list(range(10))
print(s)
print(s[0:3])
print(s[-1:])
print(s[::3])
print(s[0:-1])
s[0:1] = [-1,-1,-1]
print(s)
del s[:3]
print(s)
