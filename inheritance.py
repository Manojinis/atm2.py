class Book:
    #odd or even
    def oddoreven(self,num):
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"
    #prime number or not
    def primenumber(self,num):
        if num <= 3:
             return "Not Prime"
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                 return "Not Prime"
            return "Prime"
    def aplusb(self,a,b):
        c = (a ** 2) + (b ** 2) + (2 * a * b)
        return f"a^2+b^2= {c}"
a= int(input("Enter a number: "))
num=int(input("enter the number:"))
b=Book()
print(f"{a} is {b.oddoreven(a)}")
print(f"{num} is {b.primenumber(num)}")
print(b.aplusb(a,num))