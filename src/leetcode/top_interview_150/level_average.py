class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []

        # BFS
        result = []
        queue = [root]

        while len(queue) > 0:
            sums = 0.0
            counter = len(queue)
            for _ in range(counter):
                node = queue.pop(0)
                sums += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(sums / counter)

        return result
