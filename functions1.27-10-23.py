#functional with optional paremeters
def add(literal1: int, literal2: int, literal3: int=0):
    print(literal1 + literal2 + literal3)
add(10,20)
add(10, 20, 5)

#function with arbitary parameter:
def add_arb(*literals):
    res: int=0
    for item in literals:
        res += item
        print(res)
add_arb(1,2,3,4,5,6,7)

#arbitary key param function:
def userDetails(**literals):
    name = literals.get("name")
    email=literals.get("email")
    gender=literals.get("gender")
    print(name, email, gender)
userDetails(name="swarna", email="s@gmail.com", gender="female")

#returnable function:
def add(literal1: int, literal2: int=0, literal3: int=0):
    return literal1 +literal2 +literal3
result=add(1,2,3)
print(result)