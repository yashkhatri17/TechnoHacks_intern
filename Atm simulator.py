class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited. Your new balance is ${self.balance}"
        else:
            return "Invalid amount. Deposit amount should be greater than 0."

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return f"${amount} withdrawn. Your new balance is ${self.balance}"
        elif amount <= 0:
            return "Invalid amount. Withdrawal amount should be greater than 0."
        else:
            return "Insufficient funds. Withdrawal amount exceeds your balance."


def main():
    atm = ATM()

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            print(atm.check_balance())
        elif choice == '2':
            try:
                amount = float(input("Enter the deposit amount: "))
                print(atm.deposit(amount))
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == '3':
            try:
                amount = float(input("Enter the withdrawal amount: "))
                print(atm.withdraw(amount))
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == '4':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
