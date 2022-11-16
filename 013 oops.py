#Inheritance

class person:
    _name = "dar"
    __surname = "kal"
    yob=1992

obj = person()
print(obj)

class employee(person):
    _name = "Shankara"
    __surname = "Himalaya"
    yob = 6582
    pass
obj1= employee()
print(obj1.yob)
print(obj1._name)
print(obj1._employee__surname)

obj1= person()
print(obj.yob)
print(obj._name)
print(obj._person__surname)