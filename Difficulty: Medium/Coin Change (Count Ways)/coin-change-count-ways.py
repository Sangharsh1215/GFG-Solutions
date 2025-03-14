class Solution:
    def count(self, coins, sum):
        n = len(coins)
        dp = [[-1]*(sum+1) for _ in range (n+1)]
        def check(coins,sum, i):
            if sum <0:
                return 0
            if sum == 0:
                return 1
            if i == len(coins):
                return 0
            if dp[i][sum] != -1:
                return dp[i][sum]

            if sum > 0:
                pick = check(coins,sum-coins[i],i)
                nopick = check(coins,sum,i+1)                
            dp[i][sum] = pick + nopick
            return dp[i][sum]
                
        return check(coins,sum,0)
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        coins = list(map(int, input().strip().split()))
        sum = int(input())
        ob = Solution()
        print(ob.count(coins, sum))

        print("~")

# } Driver Code Ends