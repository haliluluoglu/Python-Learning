
def recursive_factorial(n):
    if n==0:
        return 1
    else:
        return n*recursive_factorial(n-1)

factorial=int(input("PLease enter a number which you want to calculate factorial: "))
print(recursive_factorial(factorial))