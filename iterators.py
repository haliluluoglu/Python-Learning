class TopTen():
    def __init__(self):
        self.num=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<10:
            self.num+=1
            return self.num
        else:
            raise StopIteration

values=TopTen()

print(values.__next__())
print(values.__next__())
print(values.__next__())    #SAME
print(next(values))         #SAME
print(values.__iter__())