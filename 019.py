# Data abstraction hide variable variabel will be accessed via class only so the person should know the name of the variabe to call it

class  ineuron:
    __stud = 'data science'

    def students(self):
        print("print the class of students", ineuron.__stud)


i=ineuron()
i.students()
print(i._ineuron__stud)
list()