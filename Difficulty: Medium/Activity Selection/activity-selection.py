class Solution:
    def activitySelection(self, start, finish):
        mapped = list(zip(start,finish))
        sortedlist = sorted(mapped, key = lambda x: x[1])
        
        count = 1
        last_finish = sortedlist[0][1]
        
        for i in range(1, len(sortedlist)):
            if sortedlist[i][0] > last_finish:
                count += 1
                last_finish = sortedlist[i][1]
        return count
                

#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the finish times
        finish = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, finish))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends