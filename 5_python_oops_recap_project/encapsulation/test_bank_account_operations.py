
class BankAccount:

    account_number = "ABC1234"

    def __init__(self,name:str,initial_deposit:float):
        self.name = name
        assert initial_deposit >= 1000 , "negative & zero amount is not allowed"
        self.__initial_deposit =  initial_deposit
        self.__current_balance = self.__initial_deposit

    def __str__(self):
        return (f"New bank account with ID {BankAccount.account_number} being opened for user {self.name}"
                f" with initial deposit of amount {self.__initial_deposit}")

    def __len__(self):
        return self.__current_balance

    def __del__(self):
        print("Your bank account has been successfully deleted from system")

    @property
    def current_balance(self):
        return f"Hello {self.name}, Your current account balance is {self.__current_balance}"


    def deposit_amt(self,amt:float):
        assert amt > 0, "negative & zero amount is not allowed"
        self.__current_balance = self.__current_balance + amt
        return (f"Amount {amt} being deposit successfully, "
                f"your current account balance updated to {self.__current_balance}")

    def withdraw_amt(self,amt:float):
        assert amt < self.__current_balance, f"withdraw amount should not exceed current account balance"
        assert amt < self.__current_balance - 1000, f"withdraw amount should not exceed minimum account balance limit"
        self.__current_balance = self.__current_balance - amt
        return (f"Amount {amt} being withdrawn successfully, "
                f"your current account balance updated to {self.__current_balance}")

gsk_account = BankAccount('GSK',5000000)
print(gsk_account)
print(gsk_account.current_balance)
print(gsk_account.deposit_amt(1000000))
print(gsk_account.withdraw_amt(3000000))
del gsk_account
