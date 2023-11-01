"""#global scope:
class Employee:
    firstName : str = "sony"
    lastName : str = "swarna"
emp = Employee()
print(emp.firstName)
print(emp.lastName)

#partially private:
class Employee:
    _firstName : str = "sony"
    _lastName : str = "swarna"
emp = Employee()
print(emp._firstName)

#strictly private
class Employee:
    __firstName : str = "sony"
    __lastName : str ="swarna"
emp = Employee()
print(emp.__firstName)

#globalvariable
def fullName():
    global lName
    fName = "prasa"
    lName = "prema"
fullName()
print(lName)
print(fName)  #error

#function scope
def fullName():
    global fName
    lName = "sony"
    fName = "ammu"
fullName()
print(fName)
print(lName) #error
"""
#ex of Abstraction:
class Employee:
    __firstName : str ="sony"
    __lastName : str = "swarna"
    def fullName(self):
        return self.__firstName + " " + self.__lastName
emp = Employee()
emp.__firstName = "ABC"
print(emp.fullName())
print(emp.__firstName)
