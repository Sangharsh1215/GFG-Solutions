class Solution:
    def equalPartition(self, arr):
        n = len(arr)
        tot = sum(arr)
        if tot % 2 == 1:
            return False
        arrtot = tot//2
        dp = [[-1]* (arrtot+1) for _ in range (n+1)]
        
        def check(arrtot,i):
            if arrtot == 0:
                return True
            if i >= n or arrtot < 0:
                return False
            if dp[i][arrtot] != -1:
                return dp[i][arrtot]
            
            pick = check(arrtot-arr[i], i+1) if arrtot >= arr[i] else False
            nopick = check(arrtot,i+1)
            
            dp[i][arrtot] = pick or nopick
            return dp[i][arrtot]
            
        return check(arrtot,0)
            
            
            


#{ 
 # Driver Code Starts
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends