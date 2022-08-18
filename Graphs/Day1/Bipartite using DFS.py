    
def cyclecolordfs(i,vis,adj,V,parent,color):
    
    # print(i,parent)
    for m in adj[i]:
        if not vis[m]:
            parent[m]=i
            vis[i]=True
            if color[i]==0:
                color[m]=1
            else:
                color[m]=0
            cyclecolordfs(m,vis,adj,V,parent,color)
        else:
            if m!=parent[i]:
                if color[m]==color[i]:
                    return False
    return True

def detect_cylce(V,adj):
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
            if(cyclecolordfs(i,vis,adj,V,parent,color)):
                continue
            else:
                return False
    return True

V=4
# adj=[[],[2],[1,4],[5],[2],[3,10,6],[5,7],[6,8],[7,9,11],[10,8],[5,9],[8]]  #Undirected Case
# adj=[[],[2],[1,3],[2,1]]          #Undirected Case
# adj=[[],[4,3],[4,3],[1,2],[1,2]]      #Undirected Case
# adj=[[],[2],[3],[4],[5],[2]]   #Directed Case
# adj=[[1,2,3],[0,2],[0,1,3],[0,2]] #Bipartite check
adj=[[1,3],[0,2],[1,3],[0,2]]   #Bipartite check
print(detect_cylce(V,adj))