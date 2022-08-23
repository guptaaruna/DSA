def kruskals(V,adj):
    edges=[]
    component={}
    we=0
    for i in range(V):
        for (m,n) in adj[i]:
            edges.append([n,i,m])
        component[i]=i
    edges.sort()
    for (d,u,v) in edges:
        if component[u] !=component[v]:
            we+=d
            c=component[u]
            for f in range(V):
                if component[f]==c:
                    component[f]=component[v]
    return(we)

V=3
adj=[[[1,5],[2,1]],[[0,5],[2,3]],[[0,1],[1,3]]]
print(kruskals(V,adj))