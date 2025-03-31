#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def postToInfix(self, postfix):
        st = []
        
        for c in postfix:
            if c.isalnum():
                st.append(c)
            else:
                t1 = st[-1]
                t2 = st[-2]
                
                st.pop()
                st.pop()
                
                con = '(' + t2 + c + t1 + ')'
                st.append(con)
                
        return st[0]


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        postfix = input()
        ob = Solution()
        res = ob.postToInfix(postfix)
        print(res)
        print("~")
# } Driver Code Ends