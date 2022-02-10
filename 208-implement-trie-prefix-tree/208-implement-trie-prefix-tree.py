class TrieNode:
    def __init__(self, val):
        self.d = {}
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        parent = self.root
        for i in word:
            if i not in parent.d:
                parent.d[i] = TrieNode(i)
            parent = parent.d[i]
        parent.isEnd = True

    def search(self, word: str) -> bool:
        parent = self.root
        for i in word:
            if i not in parent.d:
                return False
            parent = parent.d[i]
        return parent.isEnd

    def startsWith(self, prefix: str) -> bool:
        parent = self.root
        for i in prefix:
            if i not in parent.d:
                return False
            parent = parent.d[i]
        return True        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)