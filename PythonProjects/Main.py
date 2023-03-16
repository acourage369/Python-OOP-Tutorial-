from BankAccount import BankAccount

daniel = BankAccount('10970871', 456.47)
daniel.deposit(324)
print(daniel.get_balance())
daniel.withdraw(779.47)
print(daniel.get_balance())

gideon = BankAccount('0030304045', 567.34)
print(gideon.get_balance())
gideon.withdraw(345.67)
print(gideon.get_balance())

print(daniel.get_balance())


