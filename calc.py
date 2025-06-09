a=float(input("ENTER A NUMBER:"))
b=float(input("ENTER A NUMBER:"))
print("1.ADDITION ")
print("2.SUBTRACTION ")
print("3.MULTIPLICATION ")
print("4.DIVISION ")
choice=input("ENTER THE CHOICE(1/2/3/4):")
if choice=='1':
    print("result",(a+b))
elif choice=='2':
    print("result",(a-b))
elif choice=='3':
    print("result",(a*b))
elif choice=='4':
    print("result",(a/b))
else:
    print("INVALID INPUT")

