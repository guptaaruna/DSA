from queue import Queue
def cyclebfs(i,vis,adj,V,parent):
    q=Queue()
    q.put(i)
    vis[i]=True
    while(not q.empty()):
        j=q.get()
        # print(j)
        for m in adj[j]:
            print(j,m)
            if not vis[m] or j not in parent[m]:
                vis[m]=True
                parent[m].append(j)
                for x in parent[j]:
                    if x not in parent[m]:
                        parent[m].append(x)
                q.put(m)
            else:
                if m in parent[j]:
                    return True
    return False
    

def detect_cylce(V,adj):
    vis={}
    for i in range(V):
        vis[i]=False
    parent={}
    for k in range(V):
        parent[k]=[]
    for i in range(V):
        print(i)
        if (not vis[i]):
            if(cyclebfs(i,vis,adj,V,parent)):
                return True
    return False

V=5
# adj=[[],[2],[1,4],[5],[2],[3,10,6],[5,7],[6,8],[7,9,11],[10,8],[5,9],[8]] #undirected TRUE
# adj=[[],[2],[1,3],[2]]  #undirected False
# adj=[[],[4,3],[4,3],[1,2],[1,2]]   #undirected True
# adj=[[1],[0]] #undirected False
# adj=[[],[2],[3],[4],[5],[2]] #Directed Case True
# adj=[[1],[0]]  #Directed False
# adj=[[1],[2],[]] #Directed False
adj=[[],[3],[3],[],[1,2]] #Directed True

print(detect_cylce(V,adj))