def dijkstra(V, adj, S):
        #code here
    lis=[]
    for k in range(V):
        for [i,j] in adj[k]:
            lis.append(j)
    maxd=1+V*max(lis)
        # print(maxd)
    (d,vis)=({},{})
    for k in range(V):
        vis[k]=False
        d[k]=maxd
    d[S]=0
    print(d)
    for u in range(V):
        lis1=[]
        for i in range(V):
            if not vis[i]:
                lis1.append(d[i])
        nd=min(lis1)
        nvlis=[]
        for j in range(V):
            if nd==d[j] and vis[j]==False:
                nvlis.append(j)
        if nvlis==[]:
            break
        nv=min(nvlis)
        vis[nv]=True
        for [m,di] in adj[nv]:
            if not vis[m]:
                d[m]=min(d[m],di+d[nv])
        # print(d)
    return(d)

V=3
# adj=[[[3,9],[5,4]],[[4,4]],[[5,10]],[],[[5,3]],[]]
adj=[[[1,1],[2,6]],[[2,3],[0,1]],[[1,3],[0,6]]]
S=2
print(dijkstra(V,adj,S))