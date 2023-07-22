class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_string(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}\n"
