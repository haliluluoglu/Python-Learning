from functools import reduce

numbers=[0,1,2,3,4,5,6,7,8,9]

evens=list(filter(lambda e: e%2==0, numbers))
print(evens)
odds=list(filter(lambda o: o%2==1, numbers))
print(odds)

double_evens=list(map(lambda de: de*2, evens))
print(double_evens)
double_odds=list(map(lambda do: do*2, odds))
print(double_odds)

sum_evens=reduce(lambda a,b: a+b, evens)
sum_odds=reduce(lambda a,b: a+b, odds)
print("{} sum of even numbers".format(sum_evens))
print("{} sum of odd numbers".format(sum_odds))


