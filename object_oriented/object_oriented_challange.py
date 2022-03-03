# For this challenge, create a bank account class that has two attributes:

# owner
# balance
# and two methods:

# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
  
  def __init__(self, name, balance = 0):
    self.owner = name
    self.balance = balance
    
  def deposit(self, amount):
    self.balance += amount
    print(f"deposited {amount}\ntotal amount = {self.balance}")
  
  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
      print(f"debited {amount}\ntotal balance = {self.balance}")
    else:
      print("Not enough balance")
  
  def __str__(self):
    return f'Account Owner = {self.owner}\nAccount Balance = {self.balance}'

acct1 = Account('Bibek Mishra',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.withdraw(75)
acct1.deposit(100)
acct1.withdraw(200)