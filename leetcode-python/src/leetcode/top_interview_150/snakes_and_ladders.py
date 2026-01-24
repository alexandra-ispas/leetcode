class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        board.reverse()

        def get_coords(pos):
            x = (pos - 1) // length
            y = (pos - 1) % length
            if x % 2 == 1:
                y = length - y - 1
            return [x, y]

        length = len(board)
        queue = [[1, 0]]
        visited = set()

        while len(queue) > 0:
            pos, moves = queue.pop(0)

            for i in range(1, 7):
                next_pos = pos + i
                x, y = get_coords(next_pos)

                if board[x][y] != -1:
                    next_pos = board[x][y]
                if next_pos == length * length:
                    return moves + 1
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append([next_pos, moves + 1])
        return -1
