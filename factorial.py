
def factorial(n):
    result=1
    if (n==1) or (n==0) :
        return 1
    else:
        for i in range(2, n + 1):
            result *= i
        return result


number=int(input("Please enter a number which you want to factorial: "))
print(factorial(number))