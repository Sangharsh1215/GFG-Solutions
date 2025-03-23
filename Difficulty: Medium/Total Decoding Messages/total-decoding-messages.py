#User function Template for python3
class Solution:
	def solve(self,digits,n,i,dp):
        if i == n:
            return 1
        if digits[i] == '0':
            return 0

        if dp[i] != -1:
            return dp[i]

        one = self.solve(digits, n, i + 1, dp)
        two = 0
        if i != n - 1 and (digits[i] == '1' or (digits[i] == '2' and digits[i + 1] <= '6')):
            two = self.solve(digits, n, i + 2, dp)

        dp[i] = one + two
        return dp[i]

    def countWays(self, digits: str) -> int:
        n = len(digits)
        dp = [-1] * (n + 1)
        return self.solve(digits, n, 0, dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        digits = input()
        ob = Solution()
        ans = ob.countWays(digits)
        print(ans)
        print("~")

# } Driver Code Ends