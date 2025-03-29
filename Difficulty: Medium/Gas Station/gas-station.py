class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        totsur = 0
        currsur = 0
        ind = 0
        
        for i in range(n):
            netgain = gas[i%n] - cost[i%n]
            totsur += netgain
            currsur += netgain
            
            if currsur < 0:
                ind = i + 1
                currsur = 0
                
        return ind if totsur >= 0 else -1
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        gas = list(map(int, input().strip().split()))
        cost = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.startStation(gas, cost)
        print(ans)
        print("~")

# } Driver Code Ends