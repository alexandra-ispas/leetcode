class TrieNode(object):
    def __init__(self):
        self.is_leaf = False
        self.children = [None] * 26 * 3


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root

        for ch in word:
            idx = ord(ch) - ord("A")
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_leaf = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def dfs(idx, root):
            node = root
            for i in range(idx, len(word)):
                ch = word[i]
                if ch == ".":
                    for child in node.children:
                        if child is not None and dfs(i + 1, child):
                            return True
                    return False
                else:
                    idx2 = ord(ch) - ord("A")
                    if node.children[idx2] is None:
                        return False
                    node = node.children[idx2]

            return node.is_leaf

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
