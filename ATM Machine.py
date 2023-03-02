#This Is ATM Machine woeking Module

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful. New balance is {self.balance}."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return f"Withdrawal successful. New balance is {self.balance}."

atm = ATM(1000)  # initialize ATM with a starting balance of 1000
while True:
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Your balance is {atm.check_balance()}.")
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        print(atm.deposit(amount))
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        print(atm.withdraw(amount))
    elif choice == 4:
        print("Thank you for using our ATM!")
        break
    else:
        print("Invalid choice. Please try again.")