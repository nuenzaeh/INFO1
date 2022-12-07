#!/usr/bin/env python3
class MagicDrawingBoard:
    def __init__(self, x, y):
        if not(isinstance(x, int) and isinstance(x, int)) or x <0 or y< 0:
            raise Warning("Coordinates out of bound")
        self.lines = y
        self.rows = x
        self.board = ["0" * x for i in range(y)]


    def pixel(self, tuple):
        x = tuple[0]
        y = tuple[1]
        if (x in range(self.lines)) and y in range(self.rows):
            self.board[x] = self.board[x][:y] + "1" + self.board[x][y + 1:]
        else:
            raise IndexError

    def rect(self, start, end):
        l1 = start[1]
        l2 = end[1]
        r1 = start[0]
        r2 = end[0]
        if not (l2 >= l1 and r2 >= r1) or r1 < 0 or r2 < 0 or l1 < 0 or l2 < 0:
            raise ValueError
        if l2 > self.lines + 1 or r2 > self.rows + 1:
            raise IndexError
        for i in range(l1, l2):
            s = r2 - r1
            newline = self.board[i][:r1] + s * "1" + self.board[i][r2:]
            self.board[i] = newline

    def img(self):
        return "\n".join(self.board)

    def __repr__(self):
        return "\n".join(self.board)

    def reset(self):
        self.board = ["0" * self.rows for i in range(self.lines)]

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard("a",4)
    db.pixel((1,0))
    print(db)
    #db.rect((2,2), (6,4))
    db.reset()
    print(db)
    db.rect((2, 2), (5, 4))
    print(db)
