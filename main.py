from savings_account import SavingsAccount
from checking_account import CheckingAccount

if __name__ == "__main__":
    # Create two instances of CheckingAccount
    checking1 = CheckingAccount("Alice", 1500.0, 100.0, "ACCT-111", "ROUT-999", 500.0)
    checking2 = CheckingAccount("Bob", 800.0, 50.0, "ACCT-222", "ROUT-999", 500.0)

    # Create two instances of SavingsAccount
    savings1 = SavingsAccount("Charlie", 5000.0, 500.0, "ACCT-333", "ROUT-999", 0.03)
    savings2 = SavingsAccount("Diana", 10000.0, 1000.0, "ACCT-444", "ROUT-999", 0.04)

    # Scenario: User opens a checking account and withdraws $x
    print("--- SCENARIO 1: Withdraw from Checking ---")
    checking1.withdraw(200)
    
    # Scenario: Illustrate transfer limitation
    print("\n--- SCENARIO 2: Transfer limitation ---")
    checking1.transfer(600, savings1) # Fails (Over $500 limit)
    checking1.transfer(100, savings1) # Succeeds

    # Scenario: Illustrate interest
    print("\n--- SCENARIO 3: Apply interest ---")
    savings1.apply_interest()