class Solution:
    def isCycle(self, V, edges):
        from collections import deque, defaultdict

        def detect(src, adj, vis):
            vis[src] = 1
            q = deque()
            q.append((src, -1))

            while q:
                node, parent = q.popleft()
                for adjnode in adj[node]:
                    if not vis[adjnode]:
                        vis[adjnode] = 1
                        q.append((adjnode, node))
                    elif adjnode != parent:
                        return True
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [0] * V
        for i in range(V):
            if not vis[i]:
                if detect(i, adj, vis):
                    return True
        return False

	                
	        
	        
	        
	    

#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


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
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends