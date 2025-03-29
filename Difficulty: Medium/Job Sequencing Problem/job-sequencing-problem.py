class Solution:
    def find(self, parent, i):
        if parent[i] == i:
            return i
        parent[i] = self.find(parent, parent[i])
        return parent[i]

    def jobSequencing(self, deadline, profit):
        arr = sorted(zip(deadline, profit), key=lambda x: x[1], reverse=True)
        max_ded = max(deadline)
        parent = list(range(max_ded + 1))
        count = 0
        total_profit = 0

        for d, p in arr:
            available_slot = self.find(parent, min(d, max_ded))
            if available_slot > 0:
                parent[available_slot] = self.find(parent, available_slot - 1)
                count += 1
                total_profit += p

        return count, total_profit

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        deadline = list(map(int, input().strip().split()))
        profit = list(map(int, input().strip().split()))

        obj = Solution()
        ans = obj.jobSequencing(deadline, profit)
        print(ans[0], ans[1])
        print("~")
# } Driver Code Ends