#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        if n < 2:
            return  -1
        max1 = float('-inf')
        max2 = float('-inf')
            
        for num in arr:
            if num > max1:
                max2 = max1
                max1 = num
            elif max1 > num > max2:
                max2 = num
        return max2 if max2 != float('-inf') else -1
            
                 


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends