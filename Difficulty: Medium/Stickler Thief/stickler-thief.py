class Solution:  
    def findMaxSum(self,arr):
        n = len(arr)
        dp = [-1]* (n+1)
        
        def check(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
                
            pick = arr[i] + check(i+2)
            nopick = check(i+1)
            
            dp[i] = max(pick,nopick)
            
            return dp[i]
        return check(0)

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends