# """constructer is entity function inbuit or default method by which we will be able to pass a data or info to class"""
class person:
    def age(kbc, current_year, year_of_birth):
        return current_year - kbc.year_of_birth
# self is pointer or referal we can use any word instead of it below is the example

    # def __init__(self, name, surname, emailid, year_of_birth):
    #     self.name = name
    #     self.surname = surname
    #     self.emailid = emailid
    #     self. year_of_birth = year_of_birth

    def __init__(kbc, name, surname, emailid, year_of_birth):
        kbc.name = name
        kbc.surname = surname
        kbc.emailid = emailid
        kbc. year_of_birth = year_of_birth

    def age(kbc, current_year):
        return current_year - kbc.year_of_birth

var = person("Darshan", "Kalamkhede", "darshan220692@gmai.com", 1992)
pk = person("prime", "octa", "octa@gmai.com", "2021")
perk = person("perks", "Darimilk", "perks@gmai.com", "1996")
print(var.name)
print(pk.surname)
print(perk.emailid)
print(type(pk))
print(var.age(2022))