from bankaccount import BankAccount

# instance of a bank account
account = BankAccount("BRAINYYAWSON", "1434454676", 80)


print(f"You deposited: ${account.deposit(20)}")
print(f"You withdrew: ${account.withdraw(40)}")

print(account.get_balance())