# https://www.youtube.com/watch?v=-3rVMYGBwO0
# https://www.techinterviewhandbook.org/algorithms/graph/


def word_found_in_board(board: list[list[str]], word: str) -> bool:
    rows = len(board)
    columns = len(board[0])
    path = set()

    def dfs(row: str, column: str, index: int):
        if index == len(word):
            return True
        if row < 0 or column < 0 or row >= rows or column >= columns or word[index] != board[row][column] or (row, column) in path:
            return False
        
        path.add((row, column))
        result = dfs(row + 1, column, index + 1) or dfs(row - 1, column, index + 1) or dfs(row, column + 1, index + 1) or dfs(row, column - 1, index + 1)
        path.remove((row, column))
        return result

    for row in range(rows):
        for column in range(columns):
            if dfs(row, column, 0):
                return True
    return False
