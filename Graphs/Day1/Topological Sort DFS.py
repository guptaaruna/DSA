
def dfs(i,indegree,topsortlist,lis,adj):
    topsortlist.append(i)
    indegree[i]-=1
    for k in adj[i]:
        indegree[k]-=1
        if indegree[k]==0:
            dfs(k,indegree,topsortlist,lis,adj)
    #Function to return list containing vertices in Topological order.
def topoSort(V, adj):
    # Code here
    (indegree,topsortlist)=({},[])
    for i in range(V):
        indegree[i]=0
    for j in range(V):
        for k in adj[j]:
            indegree[k]+=1
    lis=[]
    for u in range(V):
        if indegree[u]==0:
            lis.append(u)
    # print(lis)
    for i in range(V):
        if indegree[i]==0:
            print(i)
            dfs(i,indegree,topsortlist,lis,adj) 
    # print(topsortlist)
    return(topsortlist)

V=6
adj=[[],[3],[3],[],[0,1],[0,2]]
# adj=[[],[0],[0],[0]]
print(topoSort(V,adj))
