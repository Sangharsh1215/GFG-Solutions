class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    
	    def dfs(row,col,image,ans,newColor,delrow,delcol,incolor):
	        ans[row][col] = newColor
	        n = len(image)
	        m = len(image[0])
	        for i in range(4):
	            nrow = row + delrow[i]
	            ncol = col + delcol[i]
	            
	            if (nrow >= 0) and (nrow < n) and (ncol >= 0) and (ncol < m) and (image[nrow][ncol] == incolor) and (ans[nrow][ncol] != newColor):
	                dfs(nrow,ncol,image,ans,newColor,delrow,delcol,incolor)
	                
	    
	    
	    
	    
	    incolor = image[sr][sc]
	    ans = image
	    delrow = [-1,0,1,0]
	    delcol = [0,1,0,-1]
	    dfs(sr,sc,image,ans,newColor,delrow,delcol,incolor)
	    
	    return ans



#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)

T = int(input())  # Read number of test cases
for i in range(T):
    n = int(input())
    m = int(input())

    # Reading the image matrix
    image = []
    for _ in range(n):
        image.append(list(map(int, input().split())))

    # Read starting row, column, and new color
    sr = int(input())
    sc = int(input())
    newColor = int(input())

    # Create an instance of the Solution class and apply floodFill
    obj = Solution()
    ans = obj.floodFill(image, sr, sc, newColor)

    for row in ans:
        print(" ".join(map(str, row)))
    print("~")

# } Driver Code Ends