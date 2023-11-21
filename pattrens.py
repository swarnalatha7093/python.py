def triangle(n):
    for j in range(0, n):
        for i in range(0, j):
            print("* ",end="")
        print()
triangle(5)

def triangle(n):
    x=0
    for i in range(0, n):
        for j in range(0, x):
            print(" ", end=" ")
        x=x+1
        for k in range(0, n):
            print("*",end=" ")
        n=n-1
        print("\r")
triangle(5)

def triangle(n):
    x=0
    for i in range(0, n):
        for j in range(0, x):
            print("", end="")
        x=x+1
        for k in range(0, n):
            print("*",end=" ")
        n=n-1
        print("\r")
triangle(5)

def triangle(n):
    x=0
    for i in range(0, n):
        for j in range(0, x):
            print("", end=" ")
        x=x+1
        for k in range(0, n):
            print("*",end=" ")
        n=n-1
        print("\r")
triangle(5)

def triangle(n):
    x=n-1
    for i in range(1, n):
        for j in range(0, x):
            print(" ",end=" ")
        x=x-1
        for k in range(0, i):
            print("*", end=" ")
        n=n-1
        print("\r")
triangle(5)

def triangle(n):
    x=n-1
    for i in range(1, n):
        for j in range(0, x):
            print(" ",end=" ")
        x=x-1
        for k in range(0, i):
            print("* ", end=" ")
        n=n-1
        print("\r")
triangle(6)

#fibanocci
def triangle(n):
    x = 0
    for j in range(0, n):
        lst = fibseries()
        for k in range(0, x):
            print(" ",end="")
        x = x+1
        for i in range(0, n):
            print(lst[i],end=" ")
        n = n-1
        print("\r")
def fibseries():
    return[0,1,1,2,3]
triangle(5)

def triangle(n):
    x = 0
    for j in range(0, n):
        lst = evenseries()
        for k in range(0, x):
            print(" ",end="")
        x = x+1
        for i in range(0, n):
            print(lst[i],end=" ")
        n = n-1
        print("\r")
def evenseries():
    return[2,4,6,8,10]
triangle(5)

def triangle(n):
    x = 0
    for j in range(0, n):
        lst = primeseries()
        for k in range(0, x):
            print(" ",end="")
        x = x+1
        for i in range(0, n):
            print(lst[i],end=" ")
        n = n-1
        print("\r")
def primeseries():
    return[1,2,3,5,7]
triangle(5)

