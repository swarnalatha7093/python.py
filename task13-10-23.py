#string slicing
name = "python"
print(name[0:3])
print(name[ : ])
print(name[0: ])
print(name[ : 5])
print(name[3:])

#negative index
print(name[-6:-1])
print(name[-6: ])
print(name[ :-1])

#list data type
#implicit
attendees = ["swarna","sweety","sony"]
print(type(attendees))
#explicity
attendees = list(("swarna","sweety","sony"))
print(type(attendees))
#data annotation:
attendees:list = ["swarna","sweety","sony"]
print(type(attendees))

#accesing list items:
attendees:list =["swarna","sweety","sony"]
print(attendees[0])
print(attendees[-1])
print(attendees[:])
print(attendees[0:3])
print(attendees[-2:-1])
print(attendees[-2:])

#1.reverse a string
original_string = "sony swarna"
reversed_string = original_string[::-1]
print(reversed_string)

#2nd method
original_string = "sony swarna"
reversed_string = ""
for char in reversed(original_string):
    reversed_string = reversed_string + char    #reversed_string +=char
print(reversed_string)

#2.reverse a string without a slicing
string = "sonyswarna"
newstring=""
for i in string:
    newstring=i+newstring
print(newstring)

#3.reverse of a list item
original_string = list(("swarna","sony","sweety"))
reversed_string = original_string[::-1]
print(reversed_string)

#2nd model
original_string = list(("swarna","sony","sweety"))
reversed_string = ""
for list in reversed(original_string):
    reversed_string = reversed_string + list
print(reversed_string)