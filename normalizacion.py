import numpy as np
print('ingrese dimension de la matriz:')
n= int(input())
a=[];
for i in range(n):
    row =[]
    for j in range(n):
    	row.append(float(input('A[' + str(i) + ',' + str(j) +']: ')))
    a.append(row)

print()

for i in range(n):
    for j in range(n):
        print(a[i][j], end = " ")
    print()

matrix = np.array(a)
norms = np.linalg.norm(matrix, axis=1)
print(matrix/norms)