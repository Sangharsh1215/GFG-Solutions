#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def bitManipulation(self, num, i):
        get = (num >> (i-1)) & 1
        
        setbit = num |(1 << (i-1)) 
        
        clear = num & ~(1 << (i-1))
        
        print(get,setbit,clear)
        


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, i = list(map(int, input().split()))
        ob = Solution()
        ob.bitManipulation(n, i)
        print("~")
# } Driver Code Ends