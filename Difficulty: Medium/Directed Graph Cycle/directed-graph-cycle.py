
from collections import defaultdict
class Solution:
    def isCycle(self, V, edges):
        def dfs(node,vis,pathvis,adj):
            vis[node] = 1
            pathvis[node] = 1
            
            for it in adj[node]:
                if not vis[it]:
                    if dfs(it,vis,pathvis,adj) == True:
                        return True
                elif pathvis[it]:
                    return True
            pathvis[node] = 0
            return False
        
        
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
        
        vis = [0]*V
        pathvis = [0]*V
        
        for i in range(V):
            if not vis[i]:
                if dfs(i,vis,pathvis,adj) == True:
                    return True
        return False


#{ 
 # Driver Code Starts
from collections import deque


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")


if __name__ == "__main__":
    main()

# } Driver Code Ends