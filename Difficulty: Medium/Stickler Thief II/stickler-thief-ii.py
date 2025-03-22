class Solution:
    def maxValue(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
        def check(i,end,dp):
            if i > end:
                return 0
            if dp[i] != -1:
                return dp[i]
                
            pick = arr[i] + check(i+2,end,dp)
            nopick = check(i+1,end,dp)
            
            dp[i] = max(pick,nopick)
            return dp[i]
        
        dp1 = [-1]* (n+1)
        case1 = check(0,n-2,dp1)
        
        dp2 = [-1]* (n+1)
        case2 = check(1,n-1,dp2)
        
        return max(case1,case2)



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends