class Solution:
    def maxPartitions(self , s):
        n = len(s)
        count = 0
        mp = {}
        end = 0
        size = 0
        for i,c in enumerate(s):
            mp[c] = i
            
        for i,c in enumerate(s):
            end = max(end,mp[c])
            size += 1
            
            if i == end:
                count += 1
                
        return count
            

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends