class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hori = collections.defaultdict(set)
        verti = collections.defaultdict(set)
        box = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in hori[i] or board[i][j] in verti[j] or
                   board[i][j] in box[(i//3,j//3)]):
                   return False
                else:
                    hori[i].add(board[i][j])
                    verti[j].add(board[i][j])
                    box[(i//3,j//3)].add(board[i][j])
        return True
