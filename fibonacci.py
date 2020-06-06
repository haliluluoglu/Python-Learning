def fibonacci(n):
    a=0
    b=1
    if (n==1) or (n==0):
        return 1
    else:
        for i in range(n - 1):
            c = a + b
            a, b = b, c
        return c


input_number=int(input("Please, enter .th element of number: "))
print(fibonacci(input_number))
