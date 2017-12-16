""""实现最简单的迭代器"""
class MyRange(object):
    def __init__(self,n):
        self.idx = 0
        self.n = n

    def __next__(self):
        if self.idx < self.n:
            val = self.idx
            self.idx += 1
            return val
        else:
            raise StopIteration()

    def __iter__(self):
        return self


myRange = MyRange(3)
for i in myRange:
    print(i)

"""实现斐波拉契数列"""
class Fibs(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        return self.a
Fibs = Fibs()
for i in Fibs:
    if i > 1000:
        print(i)
        break
