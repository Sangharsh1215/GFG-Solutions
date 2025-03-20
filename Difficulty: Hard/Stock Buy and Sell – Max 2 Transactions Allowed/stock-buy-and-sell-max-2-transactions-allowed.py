class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        k = 2
        dp = [[0] * n for _ in range(k+1)]
        
        for i in range(1, k+1):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i-1][j] - prices[j])
        
        return dp[k][n-1]


#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends