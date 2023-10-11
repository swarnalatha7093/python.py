
#boolean datatype: implicit
bln=True
print(type(bln))

#explicit
bln=bool(True)
print(type(bln))

#variable annotatiion
bln:bool=False
print(type(bln))

#string data type: implicit
name="swarna"
print(type(name))

#explicit
a=str(10)
print(type(a))

#variable annotation
name:str="swarna"
print(type(name))

#number system
#binary: Implicit
a = 0b1010
print(a)
print(type(a))

#explicit
a = bin(0b1010)
print(a)
print(type(a))

#data annotation
a: bin = 0b1010
print(a)
print(type(a))

#examples
a=bin(10)
print(a)

a=bin(False)
print(a)

a=bin(True)
print(a)

#octal number system implicit:
a=0O1234
print((8*8*8*1)+(8*8*2)+(8*3)+(1*4))
print(a)

#explicit
a=oct(0O1234)
print(a)
print(type(a))

#data annotation
a: oct = 0O1234
print(a)
print(type(a))

#hexa number sysytem implicit
a=0Xface
print(a)
print(type(a))

#explicit
a=hex(0X12ab)
print(a)
print(type(a))

#annotation
a:hex=0X1234
print(a)
print(type(a))