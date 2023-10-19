#intersection_update
a:set={'apple','banana','cherry'}
b:set={'banana','cherry','dragon'}
print(a.intersection_update(b))
print(a)     #{'banana','cherry'}
print(b)     #{'dragon', 'banana', 'cherry'}

#isdisjoint
a:set={'apple'}
b:set={'dragon'}
print(a.isdisjoint(b))    #True

a:set={'apple'}
b:set={'dragon','apple'}
print(a.isdisjoint(b))   #False

#difference
a:set={'apple', 'banana', 'cherry'}
b:set={'banana', 'cherry', 'dragon'}
print(a.difference(b))      #{'apple'}
print(b.difference(a))      #{'dragon'}

#symmetric_difference
a:set={'apple','banana','cherry'}
b:set={'banana','cherry','dragon'}
print(a.symmetric_difference(b))      #{'apple', 'dragon'}

#symmetric_difference_update
a:set={'apple','banana','cherry'}
b:set={'banana','cherry','dragon'}
print(a.symmetric_difference_update(b))       #None
print(a)        #{'apple', 'dragon'}
print(b)        #{'banana', 'dragon', 'cherry'}

#issubset
a:set={'apple','banana','cherry'}
b:set={'banana','cherry','dragon'}
print(a.issubset(b))     #False

a:set={'banana','cherry'}
b:set={'banana','cherry','dragon'}
print(a.issubset(b))     #True

#issuperset
a:set={'apple','banana','cherry'}
b:set={'banana','cherry','dragon'}
print(a.issuperset(b))     #False

a:set={'apple','banana','cherry'}
b:set={'banana','cherry',}
print(a.issuperset(b))     #True

#Dictionary-implicit
userDetails={'fname':'swarna','lname':'madiki','gender':'female'}
print(userDetails)
print(type(userDetails))

#explicity
userDetails=dict({'fname':'swarna','lname':'madiki','gender':'female'})
print(userDetails)
print(type(userDetails))

#data annotation:
userDetails:dict={'fname':'swarna','lname':'madiki','gender':'female'}
print(userDetails)
print(type(userDetails))

#frozenset-union
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
print(a.union(b))

#intersection
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
print(a.intersection(b))

#isdisjoint
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
print(a.isdisjoint(b))

a=frozenset(["sony"])
b=frozenset(["swarna"])
print(a.isdisjoint(b))

#issubset
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
print(a.issubset(b))

a=frozenset(["swarna"])
b=frozenset(["swarna","sweety","sanju"])
print(a.issubset(b))

#issuperset
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
print(a.issuperset(b))

a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna"])
print(a.issuperset(b))

#diffrence
a=frozenset(["sony","swarna","sweety"])
b=frozenset(["swarna","sweety","sanju"])
print(a.difference(b))
print(b.difference(a))

#symmetric_difference
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