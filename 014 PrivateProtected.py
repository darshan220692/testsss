#We can have private variable and protected variable
#We can have private function and protected function too


#Inheritance

class person:
    _name = "dar"#private Variable
    __surname = "kal"#protected Variable
    yob=1992
    #private function
    def _age(self, current_year):
        return current_year - self.yob
    #protected funciton
    def __age1(self, current_year):
        return current_year- self.yob

obj = person()
# print(obj)
# print(obj._age(2022))
# print(obj._person__age1(2022))

class employee(person):
    _name = "Naesh"
    __surname = "Kalamkhede"
    yob = 1964
obj1= employee()
print(obj1._age(2022))
print(obj1._person__age1(2022))
print(obj1._name)#call private variable
print(obj1._employee__surname)#call protected variable

# print(obj1.yob)
# obj1= person()
# print(obj.yob)
# print(obj._name)
# print(obj._person__surname)