#Multilable inheritance/Multiple inheritance/
#Multiple inheritance
class bank:
    def transaction(self):
        print("Total transaction value")
    def account_opening(self):
        print("This will show you your account open status ")
    def deposit(self):
        print("This will show your deposited amount")

class HDFC_bank:
    def hdfc_to_icici(self):
        print("transactions to icici through hdfc")

    def deposit(self):
        print("This will show your deposited amount from hdfc")
class ineuron_bank:
    def account(self):
        print("this is a ccount status in icici")
# class icici(bank, HDFC_bank):
#     pass
class icici(HDFC_bank, bank, ineuron_bank):#order of prameter is important #This is here we show multiple inheriatance
    pass


i=icici()
i.transaction()
i.account_opening()
i.hdfc_to_icici()
i.deposit()
i.account()