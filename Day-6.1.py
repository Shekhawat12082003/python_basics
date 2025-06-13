class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ₹{amount}.")
        else:
            print("⚠️ Enter a valid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"💸 Withdrew ₹{amount}.")
        else:
            print("❌ Insufficient balance or invalid amount.")

    def display_info(self):
        print(f"👤 Owner: {self.owner}")
        print(f"💰 Balance: ₹{self.get_balance()}")


account = BankAccount("Gagandeep", 1000)
account.display_info()

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  
account.display_info()

