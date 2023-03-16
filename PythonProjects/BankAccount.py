class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        return"Your current balance is : $", self.balance

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            print("Insufficient balance")
            return "Your current balance is : $", self.balance
        else:
            self.balance = self.balance - withdraw
            return "Your current balance is : $", self.balance

    def get_balance(self):
        return "Your current balance is : $", self.balance



