class BankAccount:
    bank_title = "TOO-JAS Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._routing_number = routing_number      # Protected
        self.__account_number = account_number     # Private

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.current_balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print(f"Withdrawal denied: Remaining balance would fall below minimum.")
            return False
        else:
            self.current_balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.current_balance:.2f}")
            return True

    def print_customer_information(self):
        print(f"Bank Name:       {BankAccount.bank_title}")
        print(f"Customer Name:   {self.customer_name}")
        print(f"Current Balance: ${self.current_balance:.2f}")
        print("-" * 35)