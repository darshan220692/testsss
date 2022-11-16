#method overrriding

class ineuron:
    def student(self):
        print("details of students")
    def achivers(self ):
        print(" list of achivers")
    def hall_off_fame(self):
        print("print everyone from hall of fame")

class ineuron_vision(ineuron):
    def student(self):#Method over-riding will call from child class
        print("filters student list")

iv = ineuron_vision()
iv.student()
