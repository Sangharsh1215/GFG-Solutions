from collections import defaultdict

class Solution:
    def __init__(self):
        self.timer = 0

    def articulationPoints(self, V, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(u, parent):
            visited[u] = True
            disc[u] = low[u] = self.timer
            self.timer += 1
            children = 0

            for v in adj[u]:
                if v == parent:
                    continue
                if not visited[v]:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if parent != -1 and low[v] >= disc[u]:
                        ap[u] = True
                    children += 1
                else:
                    low[u] = min(low[u], disc[v])

            if parent == -1 and children > 1:
                ap[u] = True

        visited = [False] * V
        disc = [float('inf')] * V
        low = [float('inf')] * V
        ap = [False] * V  

        for i in range(V):
            if not visited[i]:
                dfs(i, -1)

        result = [i for i, is_ap in enumerate(ap) if is_ap]
        return result if result else [-1]




#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(int(1e7))


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append([u, v])
        obj = Solution()
        ans = obj.articulationPoints(V, edges)
        ans.sort()
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends