class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and balance tracking.
    
    This class provides basic banking operations including:
    - Depositing funds
    - Withdrawing funds (with overdraft protection)
    - Checking current balance
    
    Attributes:
        balance (float): The current account balance.
    """
    
    def __init__(self):
        """Initialize a new Checkbook instance with zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit funds into the checkbook.
        
        Parameters:
            amount (float): The amount to deposit. Must be positive.
        
        Effects:
            Increases the balance by the deposited amount.
            Prints confirmation and updated balance.
        """
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
            
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw funds from the checkbook.
        
        Parameters:
            amount (float): The amount to withdraw. Must be positive.
        
        Effects:
            If sufficient funds exist, decreases the balance by the withdrawal amount.
            Prints confirmation and updated balance or error message.
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
            
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current account balance.
        
        Effects:
            Prints the current balance formatted as currency.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def get_valid_amount(prompt):
    """
    Safely get a valid positive float amount from user input.
    
    Parameters:
        prompt (str): The message to display when asking for input.
    
    Returns:
        float or None: The valid amount entered, or None if input was invalid.
    """
    while True:
        try:
            value = input(prompt)
            # Check for empty input
            if not value.strip():
                print("Error: Please enter a value.")
                continue
                
            amount = float(value)
            
            # Check for positive amount
            if amount <= 0:
                print("Error: Amount must be greater than zero.")
                continue
                
            return amount
            
        except ValueError:
            print("Error: Please enter a valid number (e.g., 100 or 50.25).")


def main():
    """
    Main program loop for the checkbook application.
    
    Provides a command-line interface for:
    - Depositing funds
    - Withdrawing funds
    - Checking balance
    - Exiting the program
    
    Includes error handling for invalid commands and numeric input.
    """
    cb = Checkbook()
    
    print("=== Simple Checkbook Application ===")
    print("Commands: deposit, withdraw, balance, exit")
    
    while True:
        try:
            action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
            
            if action == 'exit':
                print("Thank you for using the checkbook. Goodbye!")
                break
                
            elif action == 'deposit':
                amount = get_valid_amount("Enter the amount to deposit: $")
                if amount is not None:
                    cb.deposit(amount)
                    
            elif action == 'withdraw':
                amount = get_valid_amount("Enter the amount to withdraw: $")
                if amount is not None:
                    cb.withdraw(amount)
                    
            elif action == 'balance':
                cb.get_balance()
                
            else:
                print("Invalid command. Please enter one of: deposit, withdraw, balance, exit")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break
        except EOFError:
            print("\n\nEnd of input reached. Exiting...")
            break


if __name__ == "__main__":
    main()
