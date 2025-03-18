class Solution:
    def countSetBits(self, n):
        count = 0
        while n > 0:
            x = 0
            while (1 << x) <= n:
                x += 1
            x -= 1
            
            if x == 0:
                till2x = 0
            else:
                till2x = x * (1 << (x - 1))  
            
            msb2x = n - (1 << x) + 1
            
            count += till2x + msb2x
            
            n = n - (1 << x)
        
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
        print("~")
# } Driver Code Ends