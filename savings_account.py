from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate=0.02):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.current_balance * self.interest_rate
        self.deposit(interest_amount)
        print(f"Interest applied at {self.interest_rate * 100}%. Earned: ${interest_amount:.2f}")
        return interest_amount