import numpy as np
def floydwarshal(mat):
    (rows,cols)=mat.shape
    infinity=np.max(mat)*rows*rows+1
    SP=np.zeros(shape=(rows,cols,cols+1))
    for i in range(rows):
        for j in range(cols):
            SP[i,j]=infinity
    for i in range(rows):
        for j in range(cols):
            if mat[i,j]>-1:
                SP[i,j]=mat[i,j]
    for  k in range(1,cols+1):
        for i in range(rows):
            for j in range(cols):
                SP[i,j,k]=min(SP[i,j,k-1],SP[i,k-1,k-1]+SP[k-1,j,k-1])

    return(SP[:,:,cols])
# mat=np.array([[[0,0],[1,25]],[[0,0],[0,0]]])
mat=np.array([[0,25],[-1,0]])
print(floydwarshal(mat))


