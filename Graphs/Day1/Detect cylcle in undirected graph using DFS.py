    
def cycledfs(i,vis,adj,V,parent):
    
    # print(i,parent)
    for m in adj[i]:
        if not vis[m]:
            parent[m]=i
            vis[i]=True
            cycledfs(m,vis,adj,V,parent)
        else:
            if m!=parent[i]:
                return True
    return False

def detect_cylce(V,adj):
    vis={}
    for i in range(V):
        vis[i]=False
    parent={}
    for k in range(V):
        parent[k]=-1
    for i in range(V):
        # print(i)
        if (not vis[i]):
            if(cycledfs(i,vis,adj,V,parent)):
                return True
    return False

V=4
# adj=[[],[2],[1,4],[5],[2],[3,10,6],[5,7],[6,8],[7,9,11],[10,8],[5,9],[8]]  #Undirected Case True
# adj=[[],[2],[1,3],[2]]          #Undirected Case True
adj=[[],[4,3],[4,3],[1,2],[1,2]]      #Undirected Case True
# adj=[[],[2],[3],[4],[5],[2]]   #Directed Case
print(detect_cylce(V,adj))