#Create-append:
lst=["swarna", 1, True]
print(lst)
#append
lst:list=["sony","sweety"]
lst.append("swarna")
print(lst)

#insert
attendees = ["navya","vamsi","prasad"]
attendees.insert(1,"bablu")
print(attendees)

#Read-using index
attendees = ["navya","vamsi","mohan","prasad"]
print(attendees.index("vamsi"))

#count
attendees = ["navya","vamsi","prasad","sri","sri"]
print(attendees.count("sri"))
print(attendees.count("sony"))

#
attendees=["navya","vamsi","prasad","sri"]
if(attendees.count("bablu")>0):
    print(attendees.index("bablu"))

#update-by using index
attendees=["mahesh","naresh","ganesh"]
attendees[1]="suresh"
print(attendees)

#insert
lst = [1,2,3,4]
lst.insert(1,5)
print(lst)

#append
lst = [1,2,3,4]
lst.append(5)
print(lst)

#extend
attendees=["navya","vamsi","prasad"]
attendees1=["sri"]
attendees.extend(attendees1)
print(attendees)
print(attendees1)

#delete-remove
attendees = ["navya","vamsi","prasad"]
attendees.remove("vamsi")
print(attendees)

#pop with index
attendees = ["navya","vamsi","prasad"]
attendees.pop(2)
print(attendees)

#pop without index
attendees = ["navya","vamsi","prasad"]
attendees.pop()
attendees.pop()
attendees.pop()
print(attendees)
