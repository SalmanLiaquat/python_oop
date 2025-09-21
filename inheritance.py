
# INHERITANCE: A class that inherits from another class is called a subclass.
# -> helps to increase code reusability and extensibility
# A class that is inherited from is called a superclass.

'''
class Account:
    account_counter = 1000  # for unique account numbers

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.account_number = Account.account_counter
        Account.account_counter += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def show_balance(self):
        print(f"Account No: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")


# Savings Account inherits from Account
class SavingsAccount(Account):
    def __init__(self, name, balance=0, interest_rate=0.03):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New Balance: {self.balance}")


# Current Account inherits from Account
class CurrentAccount(Account):
    def __init__(self, name, balance=0, overdraft_limit=500):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        else:
            print("Overdraft limit exceeded!")


# ------------------ Menu System ------------------

accounts = {}  # Store all accounts by account number


def create_account():
    name = input("Enter account holder's name: ")
    acc_type = input("Enter account type (savings/current): ").lower()
    if acc_type == "savings":
        acc = SavingsAccount(name, 0)
    elif acc_type == "current":
        acc = CurrentAccount(name, 0)
    else:
        print("Invalid account type!")
        return
    accounts[acc.account_number] = acc
    print(f"Account created successfully! Account Number: {acc.account_number}")


def deposit_money():
    acc_no = int(input("Enter account number: "))
    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_no].deposit(amount)
    else:
        print("Account not found!")


def withdraw_money():
    acc_no = int(input("Enter account number: "))
    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: "))
        accounts[acc_no].withdraw(amount)
    else:
        print("Account not found!")


def check_balance():
    acc_no = int(input("Enter account number: "))
    if acc_no in accounts:
        accounts[acc_no].show_balance()
    else:
        print("Account not found!")


# ------------------ Main Program ------------------
while True:
    print("\n--- Bank Management System ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Exiting... Thank you for banking with us!")
        break
    else:
        print("Invalid choice! Please try again.")
'''

# multi-level inheritance

class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips
    def show(self):
        print(f"Material: {self.material}")
        print(f"Zips: {self.zips}")


class Car(Factory):
    def __init__(self,material,zips,engine):
        super().__init__(material,zips)
        self.engine = engine

    def show(self):
        print(f"Material: {self.material}")
        print(f"Zips: {self.zips}")
        print(f"Engine: {self.engine}")


class Bike(Car):
    def __init__(self,material,zips,engine,wheels):
        super().__init__(material,engine,zips)
        self.wheels = wheels

    def show(self):
        print(f"Material: {self.material}")
        print(f"Zips: {self.zips}")
        print(f"Engine: {self.engine}")
        print(f"Wheels: {self.wheels}")


obj=Bike("Metal","Zips","Engine","Wheels")
obj.show()