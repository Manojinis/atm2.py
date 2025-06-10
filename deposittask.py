dict={}
for i in range(1):
    name=input("enter the name: ")
    address=input("enter the address: ")
    phone=input("enter the phone number:")
    accno=int(input("enter the account no: "))
    dob=input("enter the dob: ")
    balance=int(input("enter the balance: "))
    pin=int(input("enter the pin:"))

dict[accno]=[name,address,phone,dob,balance]
# print(dict)
def deposit(balance):
    balance=dict[accno][-1]
    print(f"your current balance :{balance}") 
    deposit=int(input("enter deposit amount:")) 
    deposit +=2
    balance=balance+deposit
  #  print(f"your current balance {balance}") 
    dict[accno][-1]=balance
    return balance

run = True
print("Lets use the BANK ATM ....")
accno2=int(input("enter account number :"))
if accno2!=accno:
    print("account number invalid !")
    print("Enter ")
else:
    pin2=int(input("enter your pin :"))
    if pin2==pin:
         while run:
            print("1:withdraw 2:deposit 3:current balance 4:exit")
            choice=int(input("Enter your choice :"))
            if choice==1:
                balance=dict[accno][-1]
                print(f"your current balance : {balance}")
                withdraw_amt=int(input("Enter the withdraw amount : "))
                if withdraw_amt>balance:
                    print("Insuffient Balance")
                else:
                    balance=balance-withdraw_amt
                    dict[accno][-1]=balance
                    print(balance)
            if choice==2:
                a = deposit(balance)
                print(a)
            if choice==3:
                print(f"your current balance is {balance}")
                # print(balance) 
            if choice==4:
                print("You chose to Exit the atm !")
                run = False
        
    else:
        print("Invalid PIN , Please check your pin !")




print("Thank You")
