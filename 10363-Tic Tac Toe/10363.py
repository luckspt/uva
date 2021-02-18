#Accepted, based on https://www.geeksforgeeks.org/validity-of-a-given-tic-tac-toe-board-configuration/
qty = int(input())

matches = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]] 
def checkWin(board, char):
    for match in matches:
        if board[match[0]] == char and board[match[1]] == char and board[match[2]] == char:
            return True
    return False

def getAnswer(board):
    countX = inputs.count('X')
    countO = inputs.count('O')
    if countX != countO and countX != countO + 1:
        return False
    
    board = [c for c in inputs]
    oWins = checkWin(board, 'O')
    xWins = checkWin(board, 'X')
    
    if oWins:
        if xWins:
            return False
        if countX == countO:
            return True
        
    if xWins and countX != countO+1:
        return False
    if not oWins:
        return True
    return False
            

for i in range(qty):
    inputs = ''.join([input() for _ in range(3)])
    board = [c for c in inputs]
    
    print('yes' if getAnswer(board) else 'no')    
    
    if i != qty-1:
        input() #consume newline