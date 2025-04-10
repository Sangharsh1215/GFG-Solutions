import heapq

class Solution:
    def minCost(self, houses):
        n = len(houses)
        in_mst = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0

        heap = [(0, 0)]
        total_cost = 0

        while heap:
            cost, u = heapq.heappop(heap)
            if in_mst[u]:
                continue

            in_mst[u] = True
            total_cost += cost

            for v in range(n):
                if not in_mst[v]:
                    new_dist = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    if new_dist < min_dist[v]:
                        min_dist[v] = new_dist
                        heapq.heappush(heap, (new_dist, v))

        return total_cost


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []

        for _ in range(n):
            temp = list(map(int, input().split()))
            edges.append(temp)

        obj = Solution()
        print(obj.minCost(edges))
        print("~")
# } Driver Code Ends