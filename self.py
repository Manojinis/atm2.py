class Calc:
    def __init__(self,num):
        self.num=num

    def add(self):
        return self.num+1

    def sub(self):
        return self.num-1
num=int(input("ENTER A NUMBER:"))
c=Calc(num)
print(f"{c.add()}")
print(f"{c.sub()}")
