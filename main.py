class BankAccount:
    # 1. Class attribute: Title of the bank
    bank_title = "TOO-JAS Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        # 2. Instance attributes
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    # 3. Methods
    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.current_balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # 4. Check if withdrawal would violate minimum balance
        if self.current_balance - amount < self.minimum_balance:
            print(
                f"Withdrawal denied: Remaining balance (${self.current_balance - amount:.2f}) "
                f"would fall below the minimum required balance (${self.minimum_balance:.2f})."
            )
        else:
            self.current_balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.current_balance:.2f}")

    def print_customer_information(self):
        # Bank title included when customer information is printed
        print(f"Bank Name:       {BankAccount.bank_title}")
        print(f"Customer Name:   {self.customer_name}")
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")
        print("-" * 35)


if __name__ == "__main__":
    # Instance 1
    print("=== Creating Customer 1 ===")
    customer1_name = input("Enter your customer name: ")
    customer1_balance = float(input("Enter your current balance: "))
    customer1_min_balance = float(input("Enter your minimum balance: "))

    customer1 = BankAccount(customer1_name, customer1_balance, customer1_min_balance)

    dep1 = float(input("Enter deposit amount: "))
    customer1.deposit(dep1)

    with1 = float(input("Enter withdrawal amount: "))
    customer1.withdraw(with1)

    print()
    customer1.print_customer_information()

    # Instance 2
    print("=== Creating Customer 2 ===")
    customer2_name = input("Enter your customer name: ")
    customer2_balance = float(input("Enter your current balance: "))
    customer2_min_balance = float(input("Enter your minimum balance: "))

    customer2 = BankAccount(customer2_name, customer2_balance, customer2_min_balance)

    dep2 = float(input("Enter deposit amount: "))
    customer2.deposit(dep2)

    with2 = float(input("Enter withdrawal amount: "))
    customer2.withdraw(with2)

    print()
    customer2.print_customer_information()