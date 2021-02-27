import sys

def calcSoma(board, queens):
    soma = 0
    for i, queen in enumerate(queens):
        soma += board[i][queen]
    return soma

def isValid(queens, n):
    for i in range(n):
        if queens[i] == queens[n] or queens[i] - queens[n] == n-i or queens[n] - queens[i] == n-i:
            return False
    return True

SIZE = 8
mSoma = 0
def backtrack(board, queens, k):
    if k == SIZE:
        soma = calcSoma(board, queens)
        global mSoma
        if soma > mSoma:
            mSoma = soma
        return
    
    for i in range(SIZE):
        queens[k] = i

        if isValid(queens, k):
            backtrack(board, queens, k+1)

lines = sys.stdin
qtty = int(next(lines))
for _ in range(qtty):
    board = [[int(cell) for cell in next(lines).split(' ')] for _ in range(8)]

    backtrack(board, [None for _ in range(SIZE)], 0)
    print(mSoma)