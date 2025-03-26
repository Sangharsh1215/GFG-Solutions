class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search_prefix(self, s, start):
        node = self.root
        words = []
        for i in range(start, len(s)):
            if s[i] not in node.children:
                break
            node = node.children[s[i]]
            if node.is_end:
                words.append(i + 1)
        return words

class Solution:
    def wordBreak(self, s, dictionary):
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return True

            for end in trie.search_prefix(s, start):
                if dfs(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return dfs(0)



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        s = input().strip()
        dictionary = input().strip().split()
        ob = Solution()
        res = ob.wordBreak(s, dictionary)
        if res:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends