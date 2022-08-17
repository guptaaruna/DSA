def dfs_init(i,visited,adj,dfst):
    dfst.append(i)
    visited[i]=True
    for k in adj[i]:
        if not visited[k]:
            dfs_init(k,visited,adj,dfst)


def DFS(V,adj):
    visited={}
    dfst=[]
    for i in range(V):
        visited[i]=False
    i=0
    dfs_init(i,visited,adj,dfst)
    return(dfst)

V=9
adj=[[1,4],[0,2,3,4],[5],[6],[0,7],[],[],[8],[]]
print(DFS(V,adj))
    