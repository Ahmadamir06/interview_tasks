
class BankAccount():
    
    # a constructor initializes the values
    def __init__(self, account_number: int, account_holder_name: str, balance: int):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        
    def deposit(self, amount: int):
        self.balance += amount
    
    #withdraw checks if the balance is satisfied
    def withdraw(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
    
    def get_balance(self):
        return self.balance
    
    def get_account_info(self):
        return f"{self.account_holder_name}'s account {self.account_number} has a balance of {self.balance}"
    

#some tests
account = BankAccount(5254236, "Jyri", 99999)

print(account.get_account_info())
account.withdraw(999)
print(account.get_account_info())
account.deposit(300)
print(account.get_account_info())

#not allowed
account.withdraw(9000000)
print(account.get_account_info())