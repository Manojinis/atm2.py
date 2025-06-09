a = int(input("ENTER A NUMBER: "))
if a <= 1:
    print("IT IS NOT A PRIME NUMBER!!!")
else:
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            print("IT IS NOT A PRIME NUMBER!!!")
            break
    else:
        print("IT IS A PRIME NUMBER!!!!")


