

class Bank_Account:

    __BANK_NAME = 'ICBI Bank Pvt Ltd'
    __current_balance = 0

    def __init__(self, name, adhar, initial_balance):
        self.__name = name
        self.__adhar = adhar
        if type(initial_balance) is not int:
            print("Invalid amount entered ...")
        elif initial_balance < 0:
            print("Invalid amount entered ...")
        elif 0 < initial_balance < 1000 :
            print("Invalid amount entered ...")
        else:
            Bank_Account.__current_balance = self.__initial_balance = initial_balance


    def __str__(self):
        return f"Hello {self.__name}, Greetings from {Bank_Account.__BANK_NAME}!\nYou current accout balance is {Bank_Account.__current_balance}"


    def __contains__(self, phrase):
        return phrase in self.__name or phrase in self.__adhar
    

    def __gt__(self, amount):
        return Bank_Account.__current_balance > amount
    

    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_initial_balance(self):
        return self.__initial_balance
    
    # @initial_balance.setter
    # def set_initial_balance(self, amount):
    #     if amount > 0 and type(amount) is int:
    #         Bank_Account.current_balance, self.initial_balance = amount
    #     else:
    #         print("Invalid amount entered ...")

    
    def deposite_amount(self, amount):
        if amount > 0 and type(amount) is int:
            Bank_Account.__current_balance = Bank_Account.__current_balance + amount
            print(self)
        else:
            print("Invalid amount entered ")

    
    def withdraw_amount(self, amount):
        if amount < Bank_Account.__current_balance and amount > 500 and type(amount) is int:
            Bank_Account.__current_balance = Bank_Account.__current_balance - amount
            print(self)
        else:
            print("Invalid amount entered ")


account1 = Bank_Account('Ganesh K', 'ABCD1234', 1000)
print(account1)
print('Ganesh' in account1)
print(account1 > 500)
print(account1.get_name, account1.get_initial_balance)
account1.deposite_amount(500)
account1.withdraw_amount(700)
