#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        def merge(a,b):
            if not a: return b
            if not b: return a
            
            if a.data < b.data:
                result = a
                a.bottom = merge(a.bottom,b)
            else:
                result = b
                result.bottom = merge(a, b.bottom)
            result.next = None
            return result
            
        if not root or not root.next:
            return root
            
        root.next = self.flatten(root.next)
        root = merge(root, root.next)
        
        return root
        

            
        
                
            



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.bottom
    print()


def createLinkedList(lists):
    head = None
    temp = None
    for list_head in lists:
        if head is None:
            head = list_head
            temp = head
        else:
            temp.next = list_head
            temp = temp.next
    return head


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lists = []
        for _ in range(n):
            values = list(map(int, input().split()))
            head = None
            temp = None
            for value in values:
                newNode = Node(value)
                if head is None:
                    head = newNode
                    temp = head
                else:
                    temp.bottom = newNode
                    temp = temp.bottom
            lists.append(head)

        sol = Solution()
        linkedlist = createLinkedList(lists)
        head = sol.flatten(linkedlist)
        printList(head)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends