#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        i = len(post_exp) - 1
        st = []
        n = 0
        
        while n <= i:
            if post_exp[n].isalnum():
                st.append(post_exp[n])
                
            else:
                t1 = st[-1]
                st.pop()
                t2 = st[-1]
                st.pop()
                
                con = post_exp[n] + t2 + t1
                st.append(con)
                
            n += 1
            
        return st[0]


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        postfix = input()
        ob = Solution()
        res = ob.postToPre(postfix)
        print(res)
        print("~")
# } Driver Code Ends