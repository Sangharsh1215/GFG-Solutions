class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        dp = [[-1] * n for _ in range(n)]

        def check(start, end):
            if start + 1 == end: 
                return 0
            if dp[start][end] != -1:  
                return dp[start][end]

            ans = float('inf')
            for k in range(start + 1, end):
                left = check(start, k)
                right = check(k, end)
                cost = arr[start] * arr[k] * arr[end]
                ans = min(ans, left + right + cost)

            dp[start][end] = ans
            return ans

        return check(0, n - 1)

                
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().matrixMultiplication(arr)  # find the missing number
    print(s)  # print the result
    print("~")

# } Driver Code Ends