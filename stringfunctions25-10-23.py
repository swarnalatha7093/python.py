#String Transform Functions-capitalize
#Syntax:variable.capitalize()
a="swarna"
print(a.capitalize())

#Title
#syntax:variable.title()
a="swarna"
print(a.title())

#upper
#syntax:variable.upper()
a="swarna"
print(a.upper())

#lower
#syntax:variable.lower()
a="SWARNA"
print(a.lower())

#casefold
#syntax:variable.casefold()
a="SWARNA"
print(a.casefold())

#swapcase
#syntax:variable.swapcase()
a="SWArna"
print(a.swapcase())


#String Check Functions
#isnumeric
#syntax:variable.isnumeric()
a="124"
print(a.isnumeric())

#isalphanumeric
#syntax:variable.ialnum()
a="swarna6758767"
print(a.isalnum())

#isdecimal
#syntax:variable.isdecimal()
a="12123123"
print(a.isdecimal())

#isdigit
#syntax:variable.isdigit()
a="67468746"
print(a.isdigit())

#isascii
#syntax:variable.isascii()
a="swarna"
print(a.isascii())

#isupper
#syntax:variable.isupper()
a="swarna"
print(a.isupper())

#islower
#syntax:variable.islower()
a="SWARNA"
print(a.islower())

#isspace
#syntax:variable.isspace()
a=" "
print(a.isspace())

#isidentifier
#syntax:variable.isidentifier()
a="swarna12132"
print(a.isidentifier())

#isprintable
#syntax:variable.isprintable()
a="swarna"
print(a.isprintable())

#istitle
#syntax:variable.istitle()
a="swarna sony"
print(a.istitle())


#String Search Functions
#index
#syntax:variableName.index(string/char)
email="sony@gmail.com"
print(email.index("@"))

#rindex
#syntax:variableName.rindex(string/char)
email="sony@gmail@.com"
print(email.rindex("@"))

#rfind
#syntax:variableName.rfind(string/char)
email="sony@gmail@.com"
print(email.rindex("@"))

#startswith
#syntax:variableName.startswith(string/char)
email="sony@gmail.com"
print(email.startswith("swarna"))

#endswith
#syntax:variableName.endswith(string/char)
email="sony@gmail.com"
print(email.endswith("swarna"))

#list methods
#Append
#syntax:lst.append()
lst=[]
print(lst.append("sony"))
print(lst)

#insert
#syntax:lst.insert(index,item)
lst=["sony","swarna"]
print(lst.insert(1,"sweety"))
print(lst)

#Extend
#syntax:lst.extend(lst1)
name=["sony","swarna","sweety"]
name1=["santhosh","surya"]
name.extend(name1)
print(name)

#count
#syntax:lst.count(item)
name=["sony","swarna","swarna","swarna"]
print(name.count("swarna"))

#pop with index
#syntax:lst.pop(index)
name=["abc","efg","hij"]
name.pop(1)
print(name)

#pop without index
#syntax:lst.pop()
attendees=["abc","efg","hij"]
attendees.pop()
print(attendees)

#remove
#syntax:lst.remove()
a=["apple","banana","cherry"]
print(a.remove("apple"))
print(a)

#clear
#syntax:lst.clear()
a=["apple","banana","cherry"]
print(a.clear())
print(a)

#sort
#syntax:lst.sort()
a=[1,2,5,6,3]
a.sort()
print(a)

#reverse
#syntax:lst.reverse()
a=[1,2,5,6,3]
a.reverse()
print(a)

#Tuple Methods
#count
#syntax:tpl.count(item)
tpl=tuple((1,2,2,2,2,3,5,4))
print(tpl.count(2))

#index
#syntax:tpl.index(item)
tpl=tuple((1,2,3,4,5,6))
print(tpl.index(3))

#set methods
#add
#syntax:variable.add()
a={'a','b','c'}
a.add('d')
print(a)

#update
#syntax:variable.update(setvariable)
a={'a','b','c'}
b={'b','c','d'}
a.update(b)
print(a)

#remove
#syntax:variableName.remove(item)
a={'a','b','c'}
a.remove('b')
print(a)

#discard
#syntax:variableName.discard(item)
a={'a','b','c'}
a.discard('c')
print(a)

a={'a','b','c'}
a.discard('d')
print(a)

#pop
#syntax:variableName.pop()
a={'a','b','c'}
a.pop()
print(a)

#other methods of sets
#union
#syntax:variableName.union(variable)
a={'a','b','c'}
b={'b','c','d'}
print(a.union(b))

#intersection
#syntax:variableName.intersection(variable)
a={'a','b','c'}
b={'b','c','d'}
print(a.intersection(b))

#intersection update
#syntax:set1.intersection_update(set2)
a={'a','b','c'}
b={'b','c','d'}
print(a.intersection_update(b))
print(a)
print(b)

#isdisjoint
#syntax:set1.isdisjoint(set2)
a={'a'}
b={'b'}
print(a.isdisjoint(b))

#difference
#syntax:set1.difference(set2)
a={'a','b','c'}
b={'b','c','d'}
print(a.difference(b))

#symmetric difference
#syntax:set1.symmetric difference(set2)
a={'a','b','c'}
b={'b','c','d'}
print(a.symmetric_difference(b))

#symmetric difference update
#syntax:set1.symmetric difference update(set2)
a={'a','b','c'}
b={'b','c','d'}
print(a.symmetric_difference_update(b))
print(a)
print(b)

#issubset
#syntax:set1.issubset(set2)
a={'a','b','c'}
b={'b','c','d'}
print(a.issubset(b))

#issuperset
#syntax:set1.issuperset(set2)
a={'a','b','c'}
b={'b','c','d'}
print(a.issuperset(b))

#frozenset-union
#syntax:variableName.union(variable)
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
print(a.union(b))

#intersection
#syntax:variableName.intersection(variable)
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
print(a.intersection(b))

#isdisjoint
#syntax:set1.isdisjoint(set2)
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
print(a.isdisjoint(b))

a=frozenset(["sony"])
b=frozenset(["swarna"])
print(a.isdisjoint(b))

#issubset
#syntax:set1.issubset(set2)
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
print(a.issubset(b))

a=frozenset(["swarna"])
b=frozenset(["swarna","sweety","sanju"])
print(a.issubset(b))

#issuperset
#syntax:set1.issuperset(set2)
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
print(a.issuperset(b))

a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna"])
print(a.issuperset(b))

#diffrence
#syntax:set1.difference(set2)
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
print(a.difference(b))
print(b.difference(a))

#symmetric_difference
#syntax:set1.symmetric difference(set2)
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
print(a.symmetric_difference(b))

#copy
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
c1=a.copy()
c2=b.copy()
print(c1)
print(c2)