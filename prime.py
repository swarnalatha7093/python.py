n=int(input("enter any number:"))
for i in range (2,n//2+1,1):
    if(n%i==0):
        print("not a prime")
        break
else:
    print("given number is prime")
