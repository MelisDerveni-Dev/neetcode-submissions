class Solution:
    def isValidRow(self, board: List[List[str]]):
        for i in range(0, 9):
            seenNums = []
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seenNums:
                    return False
                seenNums.append(board[i][j])

        return True

    def isValidColumn(self, board: List[List[str]]):
        for i in range(0, 9):
            seenNums = []
            for j in range(0, 9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seenNums:
                    return False
                seenNums.append(board[j][i])

        return True
    def isValidSquare(self, board: List[List[str]]):
        for i in range(0 , 9 , 3):
            for j in range(0 , 9 , 3):
                seenNums = []
                for k in range(i, i+3):
                    for z in range(j, j+3):
                        if board[k][z] == ".":
                            continue
                        if board[k][z] in seenNums:
                            return False
                        seenNums.append(board[k][z])
        return True
                        



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidRow(board) and self.isValidColumn(board) and self.isValidSquare(board)
            
        