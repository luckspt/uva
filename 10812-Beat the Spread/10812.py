#Accepted
for _ in range(int(input())):
    soma, diff = [int(v) for v in input().split(' ')]

    if ((soma - diff) / 2) % 1 != 0:
        print('impossible')
    else:
        p = (soma-diff) // 2
        p2 = soma-p
        if p < 0:
            print('impossible')
        else:
            print(f'{p2} {p}')