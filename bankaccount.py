#Bank Account Class

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Account Balance: {self.balance}")
        