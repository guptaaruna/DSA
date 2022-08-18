def generate(numRows):
    l=[[1]]
    for i in range(numRows-1):
        l.append([])
        for j in range(len(l)):
            if (j-1)<0 or j==len(l)-1:
                l[i+1].append(l[i][0])
            else:
                l[i+1].append(l[i][j-1]+l[i][j])
    return l

n=5
print(generate(n))