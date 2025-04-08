from collections import defaultdict
class Solution:
    def isBridge(self, V, edges, c, d):
        def dfs(node,vis,adj,c,d):
            vis[node] = 1
            
            for it in adj[node]:
                if not vis[it] and not ((node == c and it == d) or (node == d and it == c)):

                    dfs(it,vis,adj,c,d)
            
            
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

            
        vis = [0]*V
        dfs(c,vis,adj,c,d)
        
        if vis[d] == 1:
            return False
        return True



#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)]
        edges = []

        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
            edges.append([u, v])

        c = int(input())
        d = int(input())

        obj = Solution()
        l = obj.isBridge(V, edges, c, d)

        if l:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends