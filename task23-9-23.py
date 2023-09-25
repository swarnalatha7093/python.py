#string data type
#implicit
name = "swarna"
print(name)
print(type(name))

#explicit
name = str("swarna")
print(name)
print(type(name))

#data annotation
name: str = "swarna"
print(name)
print(type(name))

#typeconverstions
#string data type to another data type
#int to str explicit
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
