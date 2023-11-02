class Employee:
    __firstName:str="sony"
    __lastName:str="swarna"
    def fullName(self):
        return self.__nameFormat(self.__firstName,self.__lastName)
    def __nameFormat(self,fName:str,lName:str):
        return f"{fName}{lName}"
emp = Employee()
emp.__firstName="ABC"
print(emp.fullName())
#print(emp.__nameFormate("sony","swarna"))

#single level:
class Address:
    __address:str = " "
    def addAddress(self,address):
        self.__address = address
    def getAddress(self):
        return self.__address
class Employee(Address):
    __firstName:str=" "
    __lastName:str=" "
    __surName:str=" "
    def setname(self, fName:str, lName:str, sName:str=" "):
        self.__firstName=fName
        self.__surName=sName
        self.__lastName=lName
    def __nameFormate(self):
        return f"{self.__firstName}{self.__lastName}{self.__surName}"
    def getFullName(self):
        return self.__nameFormate()
emp=Employee()
emp.setname(fName="sony", lName="swarna", sName="M")
emp.addAddress("Hydreabad")
print(emp.getFullName())
print(emp.getAddress())