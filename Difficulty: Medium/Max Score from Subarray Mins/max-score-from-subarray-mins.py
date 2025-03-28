class Solution:
    def pairWithMaxSum(self, arr):
        max_sum = float('-inf')
        for i in range(len(arr) - 1):
            max_sum = max(max_sum, arr[i] + arr[i + 1])
        return max_sum

    


        
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.pairWithMaxSum(a))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends