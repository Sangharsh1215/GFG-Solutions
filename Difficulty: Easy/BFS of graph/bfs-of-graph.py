#User function Template for python3
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        
        vis = [0]* len(adj)
        q = []
        q.append(0)
        vis[0] = 1
        bfs = []
        
        while q:
            node = q.pop(0)
            
            bfs.append(node)
            
            for it in adj[node]:
                if vis[it] == 0:
                    vis[it] = 1
                    q.append(it)
                    
        return bfs
                    
                

#{ 
 # Driver Code Starts
import sys


#Position this line where user code will be pasted.
def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())  # Number of vertices
        adj = []  # Adjacency list

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.bfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends