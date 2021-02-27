def transform(time):
    h = int(time / 1000000) / 2.3
    m = ((time // 10000 % 100) *99)/59 + h%1
    s = time // 100 % 100
    cc = time % 100

    print(f'{h} {m}')


transform(23595999)
print(int(23595999 / 1000000))
