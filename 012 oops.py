#Private/protected/public

class person:
    def __init__(self, name, surname, yob):
        self._name = name # "_name" is protected variable only withnin you can use this
        self.__surname = surname #"__surname" private to call append with class name like "_person__surname" classname +attribute
        self.yob = yob

sudh = person ("Sudhanshu", "Kumar", 1990)

print(sudh._name)
print(sudh._person__surname)