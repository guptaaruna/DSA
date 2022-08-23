def prims(V,adj):
    infinity=max(d for i in range(V) for j,d in adj)*V
    (visited,distance,nbr)=({},{},{})
    for u in range(V):
        (visited[u], distance[u], nbr[u])=(False,infinity,-1)

    # visited[0]=True
    distance[0]=0
    for i,d in adj[0]:
        nbr[i]=0
    
    for i in range(V):
        lis1=[]
        for i in range(V):
            if not visited[i]:
                lis1.append(distance[i])
        print(lis1)
        nd=min(lis1)
        nvlis=[]
        for j in range(V):
            if nd==distance[j] and visited[j]==False:
                nvlis.append(j)
        if nvlis==[]:
            break
        nv=min(nvlis)
        # nv=nvlis[0]
        visited[nv]=True
        for x,d in adj[nv]:
            (distance[x],nbr[x])=(min(distance[x],d), nv)

    return(nbr)

V=3
adj=[[[1,5],[2,1]],[[0,5],[2,3]],[[0,1],[1,3]]]
print(prims(V,adj))

    

    
