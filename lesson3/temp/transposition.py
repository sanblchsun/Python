matrix = [[0.5,0,0,0,0],
          [1,0.5,0,0,0],
          [1,1,0.5,0,0],
          [1,1,1,0.5,0],
          [1,1,1,1,0.5]]

matrix_t = list(zip(*matrix))

for line in matrix:
    print(line)
print('-' * 17)
for line in matrix_t:
    print(list(line))

a = [1,2,3,4,5]
b = [10,20,30,40,50]
c = [100,200,300,400,500]
args = [a,b,c]
result = list(zip(*args))
print(result)