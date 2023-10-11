"""a = int(input("Enter the Account Number :"))
b = int(input("Enter The PIN NO :"))
if a == 1234567890 and b==1234 :
    print("Account details is valid")
    print('''    Enter 1 to withdraw
    Enter 2 to balance enquiry''')
    c=int(input("enter the number :"))
    if c==1:
        d=int(input("enter the amount :"))
        if d>150000:
            print("insuffient balance")
        else:
            c = (150000-d)
            print("Amount Debited")
            print("Balance Amount :",c)
    elif(c==2):
        print(" Balance Amount = 150000")
    else:
        print("Select the Valid Number")
else:
    print("Invalid Account Number / PIN NO :")"""

acctNumber = 123456
pinNumber = 1234
balence = 150000

userAcctNumber = input("Enter acc. Number: ")
userPinNumber = input("Enter Pin Number: ")

if (userAcctNumber.isnumeric() and userPinNumber.isnumeric()):  #check acc number, pinnumber matched
    if(acctNumber == int(userAcctNumber) and pinNumber == int(userPinNumber)):  #matched - ask a question
        option = input("enter a opton 1.withdraw 2.check balence 3.deposit")
        if(option == "1" or option == "2" or option =="3"):
            if(option == "1"):  #withdraw
                withdrawAmount = input("enter amount to be withdraw:")  #check withdraw amount is number or not
                if(withdrawAmount.isnumeric()):
                    withdrawAmount = int(withdrawAmount)
                    if(balence >= withdrawAmount):
                        balence -= withdrawAmount
                        print(f'Balence amount: {balence}')
                    else:
                        print("Insufficient balence.")
                else:
                    print("Enterted invalid number.")
            elif(option == "2"): #check balence
                print(f"balence amount: { balence}")
            elif(option == "3"): #deposit
                depositAmount = input("enter amount to be deposot:")
                balence += int(depositAmount)
                print(balence)
        else:
            print("you have choosen invalid option.")
    else:
        print("enter valid account number and pin number.")
else:
    print("enter only numbers.")

