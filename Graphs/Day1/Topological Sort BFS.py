
from queue import Queue
def topoSort(V, adj):
    (indegree,topsortlist)=({},[])
    for i in range(V):
        indegree[i]=0
    for j in range(V):
        for k in adj[j]:
            indegree[k]+=1
    q=Queue()
    for u in range(V):
        if indegree[u]==0:
            print(u)
            q.put(u)
    while(not q.empty()):
        m=q.get()
        topsortlist.append(m)
        indegree[m]-=1
        for n in adj[m]:
            indegree[n]-=1
            if indegree[n]==0:
                q.put(n)
            
       
    return(topsortlist)

V=6
adj=[[],[3],[3],[],[0,1],[0,2]]
# adj=[[],[0],[0],[0]]
print(topoSort(V,adj))