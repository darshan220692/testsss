# class ineuron:
#     def __init__(self):
#         self.students1 = "Data Science"
#     def students(self):
#         print(self.students1)
#
# i = ineuron()
# i.students()
# i.students1 = "data analytics"#overriding
# i.students()

# class ineuron1:
#     def __init__(self):
#         self.__students1 = "Data Science"
#     def students(self):
#         print(self.__students1)
#
# i1 = ineuron1()
# i1.students()
# i1.__students1 = "Big Deta"
# i1.students()

class ineuron1:
    def __init__(self):
        self.__students1 = "Data Science"
    def students(self):
        print(self.__students1)
    def student_change (self, new_value):
        self.__students1 = new_value
i1 = ineuron1()
i1.students()
i1.__students1 = "Big Deta"#with the help of the object will not be able to call the re assigin any values at any point of time
i1.students()

i1.student_change("Darshan")#via class method it is possible to modify the variable this is called as encapsulaton
i1.students()