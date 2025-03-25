class Solution:
    def countWays(self, s):
        memo = {}

        def solve(left, right, isTrue):
            if left > right:
                return 0
            if left == right:
                return 1 if (s[left] == 'T') == isTrue else 0
            if (left, right, isTrue) in memo:
                return memo[(left, right, isTrue)]

            ways = 0
            for i in range(left + 1, right, 2):  # Operators are at odd indices
                leftT = solve(left, i - 1, True)
                rightT = solve(i + 1, right, True)
                leftF = solve(left, i - 1, False)
                rightF = solve(i + 1, right, False)

                if s[i] == '&':
                    if isTrue:
                        ways += leftT * rightT
                    else:
                        ways += leftF * rightF + leftT * rightF + leftF * rightT
                elif s[i] == '|':
                    if isTrue:
                        ways += leftT * rightT + leftF * rightT + leftT * rightF
                    else:
                        ways += leftF * rightF
                elif s[i] == '^':
                    if isTrue:
                        ways += leftT * rightF + leftF * rightT
                    else:
                        ways += leftT * rightT + leftF * rightF

            memo[(left, right, isTrue)] = ways  
            return ways  

        return solve(0, len(s) - 1, True)

            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        print(Solution().countWays(s))
        print("~")

# } Driver Code Ends