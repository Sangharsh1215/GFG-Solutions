from collections import deque

class Solution:
    def numIslands(self, grid):
        def bfs(row, col, vis, grid):
            n = len(grid)
            m = len(grid[0])
            vis[row][col] = 1
            q = deque()
            q.append((row, col))
            
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1), 
                          (-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            while q:
                row, col = q.popleft()
                
                for dr, dc in directions:
                    nrow, ncol = row + dr, col + dc
                    
                    if (0 <= nrow < n) and (0 <= ncol < m) and \
                       vis[nrow][ncol] != 1 and grid[nrow][ncol] == 'L':
                        vis[nrow][ncol] = 1
                        q.append((nrow, ncol))
        
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        count = 0
        
        for row in range(n):
            for col in range(m):
                if vis[row][col] != 1 and grid[row][col] == 'L':
                    count += 1
                    bfs(row, col, vis, grid)
        
        return count

#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input().strip())
        m = int(input().strip())
        grid = [input().strip().split() for _ in range(n)]

        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends