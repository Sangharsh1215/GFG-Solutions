#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def count_NGEs(self, N, arr, queries, indices):
        n = len(indices)
        l = []
        while queries > 0:
            i = indices[n-queries]
            count = 0
            
            for j in range(i,N):
                if arr[j] > arr[i]:
                    count += 1
                    
            l.append(count)
            queries -= 1
            
        return l
            


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        queries = int(input())
        indices = list(map(int, input().split()))
        ob = Solution()
        NGEs = ob.count_NGEs(N, arr, queries, indices)
        for val in NGEs:
            print(val, end = ' ')
        print()
        print("~")
# } Driver Code Ends