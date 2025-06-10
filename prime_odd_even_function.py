#odd or even
a= int(input("Enter a number: "))
def oddoreven(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
b= oddoreven(a)
print(b)
#prime number or not
num=int(input("ENTER THE NUMBER:"))
def primenumber(num):
    if num <= 1:
        return "Not Prime"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "Not Prime"
    return "Prime"
b = primenumber(num)
print(b)
