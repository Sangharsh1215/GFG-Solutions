class Solution:
	def editDistance(self, s1, s2):
	    
	    m = len(s1)
	    n = len(s2)
	    
	    dp = [[0]* (n+1) for _ in range(m+1)]
	    
	    for i in range(m+1):
	        dp[i][0] = i
	    for j in range(n+1):
	        dp[0][j] = j
	    
	    for i in range(1,m+1):
	        for j in range(1,n+1):
	            if s1[i-1] == s2[j-1]:
	                dp[i][j] = dp[i-1][j-1]
	                
	            else:
	                dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
	                
	    return dp[m][n]
	    
	    
	    


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1 = input()
        s2 = input()
        ob = Solution()
        ans = ob.editDistance(s1, s2)
        print(ans)
        print("~")

# } Driver Code Ends