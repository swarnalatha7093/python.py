#string append
#operator overloading
fname="swarna"
lname="latha"
print(fname+ " " +lname)
print("Fullname:"+fname+" "+lname)

#f' string interpolation
fname="swarna"
lname="latha"
fullname=f"{fname} {lname}"
print(fullname)
print(f"fullname:{fname}{lname}")

#string join
fname="swarna"
lname="latha"
fullname=(fname,lname)
print(" ".join(fullname))
print("fullname:",fname,lname)

#string split
#split
email="swarnalathamadiki3@gmail.com"
print(email.split("@"))

#splitlines
address: str =""" 1-144/a
stpuram
kirlampudi mandal
eastgodavri dst
"""
print(address.splitlines())

#partition
email="a@swarnalathamadiki3@gmail.com"
print(email.partition("@"))

#rpartition
email="a@swarnalathamadiki3@gmail.com"
print(email.rpartition("@"))
