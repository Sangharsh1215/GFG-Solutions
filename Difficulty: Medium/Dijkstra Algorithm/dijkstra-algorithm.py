class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        from collections import defaultdict
        import heapq
        
        INF = float('inf')
        dist = [INF]*V
        dist[src] = 0
        
        graph = defaultdict(list)
        
        for u,v,w in edges:
            graph[u].append((v,w))
            
            
        heap = [(0,src)]
        
        while heap:
            d,u = heapq.heappop(heap)
            
            if d > dist[u]:
                continue
            
            for v,w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v],v))
                    
        return dist


#{ 
 # Driver Code Starts
# Initial Template for Python 3
import sys
import heapq

# Position this line where user code will be pasted.


def main():
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v, w = map(int, input().split())
            edges.append([u, v, w])
            edges.append([v, u, w])  # Since the graph is undirected

        src = int(input())

        obj = Solution()
        res = obj.dijkstra(V, edges, src)

        print(" ".join(map(str, res)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends