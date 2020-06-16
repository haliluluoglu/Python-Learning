def topTenSquare():
    n=1
    while n<=10:
        square=n*n
        yield square
        n+=1

square_values=topTenSquare()

for i in square_values:
    print(i)