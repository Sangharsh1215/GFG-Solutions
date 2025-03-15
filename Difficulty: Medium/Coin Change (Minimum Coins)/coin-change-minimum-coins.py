class Solution:
	def minCoins(self, coins, sum):
	    n = len(coins)
	    dp = [[-1]* (sum +1) for _ in range (n+1)]
	    def check(rem_sum,i):
            if i == n or rem_sum < 0:
                return float('inf')
            if rem_sum == 0:
                return 0
            if dp[i][rem_sum] != -1:
                return dp[i][rem_sum]
            if rem_sum > 0:
                pick = 1 + check(rem_sum-coins[i],i)
                nopick = check(rem_sum,i+1)
            dp[i][rem_sum] = min(pick,nopick)
            return dp[i][rem_sum]
        result = check(sum,0)
        return result if result != float('inf') else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCoins(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends