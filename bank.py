from account import Account


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, name, balance):
        account = Account(account_number, name, balance)
        self.accounts.append(account)

    def get_account_by_number(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def deposit(self, account, amount):
        account.balance += amount

    def withdraw(self, account, amount):
        if account.balance >= amount:
            account.balance -= amount
        else:
            raise ValueError("Insufficient balance!")

    def get_all_accounts(self):
        return self.accounts
