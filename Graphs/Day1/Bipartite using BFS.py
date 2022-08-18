
from queue import Queue
import re

def cyclecolorbfs(i,vis,adj,V,parent,color):
    q=Queue()
    q.put(i)
    vis[i]=True
    while(not q.empty()):
        j=q.get()
        # print(j)
        for m in adj[j]:
            if not vis[m]:
                vis[m]=True
                parent[m]=j
                if color[j]==0:
                    color[m]=1
                else:
                    color[m]=0
                q.put(m)
            else:
                if m!=parent[j]:
                    if color[m]==color[j]:
                        return False                    
    return True
    

def bipartite(V,adj):
    vis={}
    for i in range(V):
        vis[i]=False
    parent={}
    for k in range(V):
        parent[k]=-1
    color={}
    for k in range(V):
        color[k]=-1
    for i in range(V):
        # print(i)
        if (not vis[i]):
            if(cyclecolorbfs(i,vis,adj,V,parent,color)):
                continue
            else:
                return False
            
    return True

V=4
# adj=[[],[2],[1,4],[5],[2],[3,10,6],[5,7],[6,8],[7,9,11],[10,8],[5,9],[8]]
# adj=[[],[2],[1,3],[2,1]]
# adj=[[],[4,3],[4,3],[1,2],[1,2]]
# adj=[[],[2],[3],[4],[5],[2]]
adj=[[1,3],[0,2],[1,3],[0,2]] #Bipartite check
# adj=[[1,2,3],[0,2],[0,1,3],[0,2]] #Bipartite check
print(bipartite(V,adj))