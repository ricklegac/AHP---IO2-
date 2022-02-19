import numpy as np
print('ingrese dimension de la matriz:')
n= int(input())

for i in range(n):
    row =[]
    for j in range(n):
    	row.append(int(input('A[' + str(i) + ',' + str(j) +']: ')))
    a.append(row)

print()

for i in range(n):
    for j in range(n):
        print(a[i][j], end = " ")
    print()

matrix = np.array([[1,2],[3,4]])
norms = np.linalg.norm(matrix, axis=1)
print(matrix/norms)