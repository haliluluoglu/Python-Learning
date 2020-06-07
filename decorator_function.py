#This decorator aims to divide two numbers only if dividend is greater or equal from divisor.
#Otherwise, apply new decorator two swap those numbers.

def smart_divide(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    print(a/b)

divide(2,4)