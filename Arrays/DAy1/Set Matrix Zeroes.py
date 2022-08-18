def setZeroes(matrix):
    (row,col)=(len(matrix),len(matrix[0]))
    row0=[]
    col0=[]
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0:
                if i not in row0:
                    row0.append(i)
                if j not in col0:
                    col0.append(j)

    for i in row0:
        for j in range(col):
            matrix[i][j]=0
    for i in col0:
        for j in range(row):
             matrix[j][i]=0
    return matrix

matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(matrix))