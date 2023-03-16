class BankAccount:

    def __init__(self, account_name, account_number, balance):

        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        return self.balance

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            return f"Insufficient fund \n Current balance {BankAccount.get_balance(self)}"
        else:
            self.balance -= withdraw
            return self.balance

    def get_balance(self):
        return f"Your current balance is: ${self.balance}"
