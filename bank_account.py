class BankAccount:
    bank_title = "TOO-JAS Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

        # Protected member (convention: single underscore, accessible to subclasses)
        self._account_number = account_number

        # Private member (convention: double underscore, mangled outside this class)
        self.__routing_number = routing_number

    # Public getters to access encapsulated data
    def get_routing_number(self):
        return self.__routing_number

    def get_account_number(self):
        return self._account_number

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"[{self.customer_name}] Deposited ${amount:.2f}. New Balance: ${self.current_balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print(
                f"[{self.customer_name}] Withdrawal denied: Remaining balance (${self.current_balance - amount:.2f}) "
                f"would fall below minimum balance (${self.minimum_balance:.2f})."
            )
            return False
        else:
            self.current_balance -= amount
            print(f"[{self.customer_name}] Withdrew ${amount:.2f}. New Balance: ${self.current_balance:.2f}")
            return True

    def print_customer_information(self):
        print(f"Bank Name:       {BankAccount.bank_title}")
        print(f"Customer Name:   {self.customer_name}")
        print(f"Account Number:  {self._account_number}")
        print(f"Routing Number:  {self.__routing_number}")
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")
        print("-" * 35)