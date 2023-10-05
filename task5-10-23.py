accnumber=123456789
pin=12345
amount=150000
m = int(input("enter the account number: "))
if(m == accnumber):
    print("valid account")
else:
    print("not valid account")
n = int(input("enter the pin code: "))
if(n == pin):
    print("valid account")
else:
    print("not valid account")
if accnumber == 123456789 and pin == 12345:
    print("Account number is valid")
    print("select the number 1 is withdraw option.")
    print("select the number 2 is balance enquiry option.")
    option = int(input("click the option 1 or 2: "))
    if option == 1:
        debit=int(input("how much amount withdraw: "))
        if(debit>150000):
            print("Insufficient balance.")
        else:
            option=(150000-debit)
            print("Amount succesfully debited")
            print("your bank balance:",option)
    elif(option==2):
        print("total bank balnce = 150000")
    else:
        print("click the valid option")
else:
    print("invalid accnumber and pin:")
    print("please enter the valid details.")







