# suppose if we have two constructor in one class
# it will take the latest one
# but if parameter == to number of arguments then that constructer will be called
class person:
    def __init__(self, name, emailid, contNo, date_of_birth):
        self.name = name
        self.emailid = emailid
        self.contNo = contNo
        self.date_of_birth = date_of_birth

    def __init__(self, name, emailid):
        self.name = name
        self.emailid = emailid

func=person("darshan", "darshan220692@gmail.com")

print(func.name)