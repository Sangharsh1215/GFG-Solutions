from collections import deque

class Solution:
    def orangesRotting(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        q = deque()
        vis = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    q.append((i, j, 0))
                    vis[i][j] = 2
        
        tm = 0
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        
        while q:
            r, c, t = q.popleft()
            tm = max(tm, t)
            
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                
                if (0 <= nrow < n) and (0 <= ncol < m) and mat[nrow][ncol] == 1 and vis[nrow][ncol] == 0:
                    q.append((nrow, ncol, t + 1))
                    vis[nrow][ncol] = 2
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and vis[i][j] == 0:
                    return -1
        
        return tm

	           
	           
	           
	       
	            


#{ 
 # Driver Code Starts
from queue import Queue

T = int(input())
for i in range(T):
    n = int(input())
    m = int(input())
    mat = []
    for _ in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    obj = Solution()
    ans = obj.orangesRotting(mat)
    print(ans)
    print("~")

# } Driver Code Ends