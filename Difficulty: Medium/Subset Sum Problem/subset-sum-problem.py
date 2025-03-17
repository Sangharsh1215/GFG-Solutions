class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        dp = [[-1]* (sum+1) for _ in range (n+1)]
        
        def check(sum,i):
            
            if sum == 0:
                return True
            if i >= n or sum < 0:
                return False
            if dp[i][sum] != -1:
                return dp[i][sum]
                
            pick = check(sum-arr[i],i+1)
            nopick = check(sum,i+1)
            
            dp[i][sum] = pick or nopick
            return dp[i][sum]
            
        return check(sum,0)
            
            
            
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends