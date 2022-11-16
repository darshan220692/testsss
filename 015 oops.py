import logging
logging.basicConfig(filename="abc.log", level=logging.DEBUG )
class car:
    def __init__(self, body, engin, tyre):
        self.body=body
        self.engin=engin
        self.tyre = tyre
    def milage(self):
        print("Milage of this car ")
c = car("metallic", "bs7", "rubber")

print (c)
class tata(car):
    pass
t =tata("metallic", "bs7", "rubber")

print(t.milage())