class Solution:
	def minJumps(self, arr):
	    n = len(arr)
	    if n == 1:
	        return 1
	    if arr[0] == 0:
	         return -1
	         
	    maxreach = arr[0]
	    steps = arr[0]
	    jumps = 1
	    
	    for i in range(1,n):
	        if i == n-1:
	            return jumps
	            
	        maxreach = max(maxreach, i + arr[i])
	        steps -= 1
	        
	        if steps == 0:
    	        jumps += 1
    	        if i >= maxreach:
    	            return -1
    	        steps = maxreach - i
	        
	    return -1
	    # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends