qty = int(input())

for i in range(qty):
    board = ''.join([input() for _ in range(3)])

    qtd = [board.count('X'), board.count('O')]
    if qtd[0] == qtd[1] or qtd[0] == qtd[1]+1:
        print('yes')
    else:
        print('no')
    
    if i != qty-1:
        input() #consume newline