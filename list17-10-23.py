#clear
attendees = ["swarna","sony","sweety"]
print(attendees.clear())
print(type(attendees))
print(attendees)

#delete
attendees = ["swarna","sony","sweety"]
del attendees[0]
print(attendees)

#example
attendee1 = input("enter attendee name:")
attendee2 = input("enter attendee name:")
attendee3 = input("enter attendee name:")
attendees=[]
attendees.append(attendee1)
attendees.append(attendee2)
attendees.append(attendee3)
print(attendees)

#sort list
lst = [1,99,4,65,3,6,8,10]
lst.sort()
print(lst)

#reverse
lst=[1,3,45,8678,2334]
lst.reverse()
print(lst)

#tuple-implicit
tpl = (1,2,3)
print(type(tpl))

#explicty
tpl = tuple((1,2,3,4))
print(tpl)
print(type(tpl))

#count
tpl = tuple((1,2,3,1))
print(tpl.count(1))

#index
tpl = tuple((1,2,3,1))
print(tpl.index(2))

#example
tpl = tuple((1,2,3,1))
lst = list(tpl)
print(lst)

#data annotatoion
tpl:tuple=1,2,3,4
print(tpl)

#sort function with out using sorting method
l1 = [76, 23, 45, 12, 54, 9]
print("Original List:", l1)
for i in range(0, len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j], l1[i]
print("Sorted List", l1)