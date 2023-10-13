"""
first model:
num = int(input("Enter any number: "))
n1, n2 = 0, 1
sum = 0
if num<=0:
    print("Please enter number greater than 0")
else:
    for i in range (0, num):
        print(sum, end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2



second model:
num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()"""


n = 10
a = 1
b = 0
i = 1
while i<= n:
    print(b)
    a = a + b
    b = a - b
    i += 1