#left shift operator
#>>
a=4
b=2
print(a>>b)
a=5
b=8
print(a>>b)
#right shift operator
a=8
b=9
print(a<<b)
a=1
b=2
print(a<<b)
#check address of a variable
a=111
print(id(a))
a=890
print(id(a))
#identity operator
#is
a=50
b=40
print(a is b)
a=30
b=30
print(a is b)

#is not
a=10
b=19
print(a is not b)
a=13
b=13
print(a is not b)

#membership operator
#in
a="jyothi@gmail.com"
print("@" in a)
print("jyothi" in a)
print("9" in a)
fastfood=["biryani", "fired rise", "noodles"]
name = "biryani"
print(name in fastfood)
name = "jyothi"
print(name in fastfood)
#not in
names=["swarna" ,"amani" ,"sathya"]
name = "jyothi"
print(name not in names)
name = "swarna"
print(name not in names)
