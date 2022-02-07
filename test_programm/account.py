class Account:
    def __init__(self):
        self.__number=""
        self.__account=""
        self.__balance=""

    def set_number(self, number):
        self.__number=number
    def get_number(self, number):
        return self.__number

    def set_account(self, account):
        self.__account=account

    def get_account(self, account):
        return self.__account

    def set_deposit(self, deposit):
        self.__deposit = deposit
    def get_withdraw(self, withdraw):
        return self.__withdraw

a = Account
a.set_number("123")
a.set_account("Name")
a.set_deposit("5000")
print("Number :", a.get_number())
print("Account no. :",a.get_account())
print("Deposit")