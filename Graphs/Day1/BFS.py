from queue import Queue

def BFS(V,adj):
    visited={}
    bfst=[]
    for i in range(V):
        visited[i]=False
    q=Queue()
    q.put(0)
    visited[0]=True
    bfst.append(0)
    while(not q.empty()):
        j=q.get()
        for k in adj[j]:
            if not visited[k]:
                bfst.append(k)
                visited[k]=True
                q.put(k)
    return(bfst)
    
V=9
adj=[[1,4],[0,2,3,4],[5],[6],[0,7],[],[],[8],[]]
print(BFS(V,adj))
