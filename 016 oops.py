#Multilable inheritance/Multiple inheritance/
#Multilable inheritance
class bank:
    def transaction(self):
        print("Total transaction value")
    def account_opening(self):
        print("This will show you your account open status ")
    def deposit(self):
        print("This will show your deposited amount")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("transactions to icici through hdfc")

class icici(HDFC_bank):
    pass
i=icici()
i.transaction()
i.account_opening()
i.hdfc_to_icici()

