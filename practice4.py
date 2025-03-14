# __init__ Method & self Understanding
# Problem: Digital Wallet System
# Create a Wallet class that:
# Initializes with owner_name and balance.
# Implements deposit(amount) to add money.
# Implements withdraw(amount) ensuring balance never goes negative.
# Implements get_balance() to return the balance.

class Wallet:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} added to {self.owner_name}'s wallet.")
        else:
            print("Invalid amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from {self.owner_name}'s wallet.")

    def get_balance(self):
        return f"{self.owner_name}'s wallet balance: {self.balance}"

my_wallet = Wallet("Ayesha", 10000)
print(my_wallet.get_balance())

my_wallet.deposit(500)

# Withdraw money:
my_wallet.withdraw(1000)
my_wallet.withdraw(20000)

print(my_wallet.get_balance()) 

        
