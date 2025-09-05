class TrieNode(object):
    def __init__(self):
        self.is_leaf = False
        self.children = [None] * 26


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            idx = ord(ch) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_leaf = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()

        for word in words:
            trie.insert(word)

        result = []

        def dfs(node, i, j, path):
            if node.is_leaf:
                result.append(path)
                node.is_leaf = False

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return

            ch = board[i][j]
            idx = ord(ch) - ord("a")

            if ch >= "a" and node.children[idx] is not None:
                board[i][j] = "."

                dfs(node.children[idx], i - 1, j, path + ch)
                dfs(node.children[idx], i, j - 1, path + ch)
                dfs(node.children[idx], i + 1, j, path + ch)
                dfs(node.children[idx], i, j + 1, path + ch)

                board[i][j] = ch
            else:
                return

        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(trie.root, i, j, "")

        return result
