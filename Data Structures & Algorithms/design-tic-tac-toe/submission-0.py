'''
1. simulate the whole board and check for the row/col if a player wins every turn.

2. simply have a integer for each row/col and add/substract each time a player plays.
if it reaches -n/n then you know a player won
'''
class TicTacToe:

    def __init__(self, n: int):
        self.rows, self.cols = [0] * n, [0] * n
        self.diagonal = 0
        self.antiDiagonal = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        currentPlayer = 1 if player == 1 else -1

        self.rows[row] += currentPlayer
        self.cols[col] += currentPlayer

        if row == col:
            self.diagonal +=  currentPlayer
        if col == (len(self.cols) - row - 1):
            self.antiDiagonal += currentPlayer

        if (self.n == abs(self.rows[row]) or 
            self.n == abs(self.cols[col]) or 
            self.n == abs(self.diagonal) or 
            self.n == abs(self.antiDiagonal)):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
