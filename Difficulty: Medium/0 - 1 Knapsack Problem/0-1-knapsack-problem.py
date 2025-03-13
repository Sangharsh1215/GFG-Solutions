class Solution:
    def knapsack(self, W, val, wt):
        dp = [[-1 for _ in range(W + 1)] for _ in range(len(val) + 1)]
        def solve(W,val,wt,i):
            if i == len(wt):
                return 0
            if dp[i][W] != -1:
                return dp[i][W]
            nopick = solve(W,val,wt,i+1)
            pick = 0
            if W >= wt[i]:
                pick = val[i] + solve(W-wt[i],val,wt,i+1)
            dp[i][W] = max(pick,nopick)
            return dp[i][W]
        return solve(W,val,wt,0)


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        capacity = int(input())
        values = list(map(int, input().strip().split()))
        weights = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapsack(capacity, values, weights))
        print("~")
# } Driver Code Ends