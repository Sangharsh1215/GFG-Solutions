#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def preToInfix(self, pre_exp):
        n = len(pre_exp) - 1
        st = []
        
        while n >= 0:
            if pre_exp[n].isalnum():
                st.append(pre_exp[n])
                
            else:
                t1 = st[-1]
                st.pop()
                t2 = st[-1]
                st.pop()
                
                con = '(' + t1 + pre_exp[n] + t2 + ')'
                
                st.append(con)
            n -= 1
                
        return st[0]
            


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        prefix = input()
        ob = Solution()
        res = ob.preToInfix(prefix)
        print(res)
        print("~")
# } Driver Code Ends