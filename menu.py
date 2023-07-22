from bank import Bank
from file_handler import read_data, write_data


def main_menu():
    bank = Bank()
    bank_file = "bank_data.pkl"
    bank.accounts = read_data(bank_file)

    while True:
        print("\n***** Bank Management System *****")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Display All Accounts")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter Account Number: ")
            name = input("Enter Name: ")
            balance = float(input("Enter Initial Balance: "))
            bank.create_account(account_number, name, balance)
            write_data(bank_file, bank.accounts)
            print("Account created successfully!")

        elif choice == '2':
            account_number = input("Enter Account Number: ")
            account = bank.get_account_by_number(account_number)
            if account:
                amount = float(input("Enter Deposit Amount: "))
                bank.deposit(account, amount)
                write_data(bank_file, bank.accounts)
                print("Deposit successful!")
            else:
                print("Account not found!")

        elif choice == '3':
            account_number = input("Enter Account Number: ")
            account = bank.get_account_by_number(account_number)
            if account:
                amount = float(input("Enter Withdrawal Amount: "))
                try:
                    bank.withdraw(account, amount)
                    write_data(bank_file, bank.accounts)
                    print("Withdrawal successful!")
                except ValueError as e:
                    print(e)
            else:
                print("Account not found!")

        elif choice == '4':
            account_number = input("Enter Account Number: ")
            account = bank.get_account_by_number(account_number)
            if account:
                print(f"Balance: {account.balance}")
            else:
                print("Account not found!")

        elif choice == '5':
            accounts = bank.get_all_accounts()
            if accounts:
                print("Accounts List:")
                for account in accounts:
                    print(account.to_string())
            else:
                print("No accounts found!")

        elif choice == '0':
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()
