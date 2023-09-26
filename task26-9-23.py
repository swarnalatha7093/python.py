#string transform funtions:
#capitalize
a= "hi how are you ?"
print(a.capitalize())

#Titile
a="swarna"
print(a.title())

#upper
a="swarna"
print(a.upper())

#lower
a="swarna"
print(a.lower())

#casefold
a="SWARNA"
print(a.casefold())

#swapecase
a="swarna"
print(a.swapcase())

#string check functions
#isnumaric
a="123"
print(a.isnumeric())

#isalnum
a="swarna123"
print(a.isalnum())

a="@##$%asdfs"
print(a.isalnum())

#isdecimal
s = "12345"
w = "12swarna34"
a= "1278**34"
print(s.isdecimal())
print(w.isdecimal())
print(a.isdecimal())

#isdigit
a="1234"
b="12hjfhf45"
print(a.isdigit())
print(b.isdigit())

#isascii
a="sdfdff1312412"
print(a.isascii())

#isupper
a="SWARNA"
b="swarna"
print(a.isupper())
print(b.isupper())

#islower
a="swarna"
b="SWARNA"
print(a.islower())
print(b.islower())

#isspace
a="43865"
b="hi how are you"
c=" "
d="asd686"
print(a.isspace())
print(b.isspace())
print(c.isspace())
print(d.isspace())

#isidentifier
a="swarna"
b="1234"
c="sdasf132124"
d="@#$%%"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

#isprintable
a=("sdsf243235%@%^^")
print(a.isprintable())

#istitile
a="Swarna"
b="swarna"
print(a.istitle())
print(b.istitle())
