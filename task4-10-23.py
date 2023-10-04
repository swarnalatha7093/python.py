a=int(input("enter a number: "))
b=int(input("enter b number: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a&b)
print(a|b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)

#prime number
n=int(input("enter any number:"))
for i in range (2,n//2+1,1):
    if(n%i==0):
        print("not a prime")
        break
else:
    print("given number is prime")

#even or not
n=int(input("enter a number: "))
if(n%2==0):
    print("even number")
else:
    print("odd number")

#palindrame
n=int(input("Enter a number: "))
m=n
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
if(m == rev):
    print("palindrame")
else:
    print("not palindrame")

#armstrong number:
num = 153
sum_ = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum_ += digit ** 3
   temp //= 10
   
if num == sum_:
   print(num,"is an Armstrong number")
else:
   print(num,"is notArmstrong")
    
#address
address=(input("Enter a House number:"))
if "1-144/a" in address:
    print("valid")
else:
    print("not valid")

#state
address = (input("Enter a State:"))
if "Andhrapradesh" in address:
    print("valid")
else:
    print("not valid")

#village
address = (input("Enter a village:"))
if "stpuram" in address:
    print("valid")
else:
    print("not valid")



