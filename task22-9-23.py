#Decimal number system
#integer number system
#implicit
num = 10
print(num)
print(type(num))

#explicit
num = int(10.20)
print(num)
print(type(num))

#data annotation
num: int = 10
print(num)
print(type(num))

#Float number system

#implicit
num = 10.27
print(num)
print(type(num))

#explicit
num = float (10.10)
print(num)
print(type(num))

#data annotation
num: float = 10.101
print(num)
print(type(num))

#exponential
num=float(33333333333333333333333333333333334444444444444444444444444444)
print(num)
print(type(num))

#ex
num = 1.2e2
print(num)

#complex numbers-implicit
a = 1+2j
b = 3+4j
print(a+b)
print(type(a+b))
print(a.real)
print(a.imag)

#explicit
a=complex(1)
print(a)

#data annotation
a: complex=1
ex = 1
print(a)
num=1.2e4
print(num)

#typeconverstions

#str explicit
a = str(10)
print(type(a))
print(a)

#bool to str
a= str(True)
print(type(a))
print(a)

#binary to str
a= str(0b1010)
print(type(a))
print(a)

#octal to str
a= str(0o1234)
print(type(a))
print(a)

#hexa to str
a= str(0xface)
print(type(a))
print(a)

#int-str
a= str(6789)
print(type(a))
print(a)

#float-str
a= str(10.10)
print(type(a))
print(a)

#exp-str
a= str(1.2e2)
print(type(a))
print(a)

#complex-str
a= str(1+2j)
print(type(a))
print(a)

#boolean type converstions

#str-bool
a=bool("ghfh")
print(type(a))
print(a)

#bin-bool
a=bool(0b0000)
print(type(a))
print(a)

#oct-bool
a=bool(0o00110)
print(type(a))
print(a)

#hex-bool
a=bool(0x0000)
print(type(a))
print(a)

#int-bool
a=bool(1234)
print(type(a))
print(a)

#float-bool
a=bool(45.87)
print(type(a))
print(a)

#exp-bool
a=bool(1.2e2)
print(type(a))
print(a)

#com-bool
a=bool(1+2j)
print(type(a))
print(a)

#binary type converstions

#bool-bin
a=bin(False)
print(type(a))
print(a)

#oct-bin
a=bin(0o1234)
print(type(a))
print(a)

#hex-bin
a=bin(0x1234)
print(type(a))
print(a)

#int-bin
a=bin(1234)
print(type(a))
print(a)

#octal type converstiona

#bool-oct
a=oct(False)
print(type(a))
print(a)

#hex-oct
a=oct(0x1234)
print(type(a))
print(a)

#int-oct
a=oct(1234)
print(type(a))
print(a)

#bin-oct
a=oct(0b1010)
print(type(a))
print(a)

#hexadecimal type converstiona

#bool-hex
a=hex(False)
print(type(a))
print(a)

#bin-hex
a=hex(0x1234)
print(type(a))
print(a)

#int-hex
a=hex(1234)
print(type(a))
print(a)

#oct-hex
a=hex(0o1010)
print(type(a))
print(a)
