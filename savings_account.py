from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate=0.02):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.current_balance * self.interest_rate
        self.current_balance += interest_amount
        print(f"[{self.customer_name}] Interest applied at {self.interest_rate * 100:.1f}%. Earned: ${interest_amount:.2f}. New Balance: ${self.current_balance:.2f}")
        return interest_amount