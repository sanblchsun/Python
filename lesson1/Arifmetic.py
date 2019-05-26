a = 1
b = 2
c = a + b
a+=2
#assert c ==a+b

print(1+1,3-2,2*2,7/4,5%3)

print(2**1000)


print(3<4<6,3>=5)
print(1<<8,4>>2,~4)
for i,j in (0,0),(0,1),(1,0),(1,1):
    print (i,j,":",i&j,i|j,i^j)

for i,j in (0,False),(1,True):
    print(i,":",j)

for i in (False,True):
    for j in (False, True):
        print(i,j,":",i and j, i or j, not i)

s1 = "строка1"
s2 = 'строка2\nс переводом стоки внутри'
s3 = """строка3
с переводом строки внутри"""
u1 = u'\u043f\u0440\u0438\u0432\u0435\u0442'  # привет
u2 = u'Еще пример'    # не забудьте про coding!
print(s1,'\n',s2,'\n',s3,'\n',u1,'\n',u2)

arf = r"(\d)=\1"

print (arf)

print("A" + "B")
print("A"*10)
print("%s %i" % ("abc",12))
