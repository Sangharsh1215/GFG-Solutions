#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, s):
        prec = {'^':3, '*':2, '/':2, '+':1, '-':1}
        out = []
        stack = []
        
        for c in s:
            if c.isalnum():
                out.append(c)
            elif c == '(':
                stack.append(c)
            elif c == ')':
                while stack and stack[-1]!='(':
                    out.append(stack.pop())
                stack.pop()
                
            else:
                while stack and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                    out.append(stack.pop())
                    
                stack.append(c)
        while stack:
            out.append(stack.pop())
        return ''.join(out)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        exp = str(input())
        ob = Solution()
        print(ob.InfixtoPostfix(exp))
        print("~")

# } Driver Code Ends