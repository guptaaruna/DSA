def bellman_ford(V, adj, S):
    d=[]
    for k in range(V):
        d.append(100000000)
    d[S]=0    
    for i in range(V-1):  
        for [m,n,p] in adj:
            d[n]=min(d[n],p+d[m])
    return(d)


V=3
S=2
adj=[[0,1,5],[1,0,3],[2,0,1]]
print(bellman_ford(V,adj,S))