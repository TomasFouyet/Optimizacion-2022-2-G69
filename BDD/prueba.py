
from matrix import construir_matrix

matrix = construir_matrix()
Q_fjk = 0
for i in range(0,len(matrix)):
    familia = i
    for j in range (0,len(familia[i])):
        if j == 1 or j == 2 or j == 3:
            caja = j
            muni = (j // 3) + 1
        else:
            caja = j % 3
            muni = (j // 3) + 1
        if matrix[i][j] == 1:
            Q_fjk[familia, caja, muni] = 1
        else:
            Q_fjk[familia, caja, muni] = 0

        
        

        