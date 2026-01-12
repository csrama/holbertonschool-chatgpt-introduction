#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.
    
    Parameters:
    -----------
    n : int
        The non-negative integer for which to calculate the factorial.
        Must be >= 0.
    
    Returns:
    --------
    int
        The factorial of n (n! = n × (n-1) × ... × 2 × 1)
        Returns 1 when n is 0.
    
    Raises:
    -------
    ValueError
        If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Main execution
if __name__ == "__main__":
    # Check if argument is provided
    if len(sys.argv) != 2:
        print("Usage: ./factorial_recursive.py <number>")
        print("Example: ./factorial_recursive.py 5")
        sys.exit(1)
    
    try:
        # Convert argument to integer
        number = int(sys.argv[1])
        
        # Calculate factorial
        result = factorial(number)
        
        # Print result
        print(result)
        
    except ValueError as e:
        if "invalid literal" in str(e):
            print(f"Error: '{sys.argv[1]}' is not a valid integer")
        else:
            print(f"Error: {e}")
        sys.exit(1)
    except RecursionError:
        print("Error: Number is too large for recursive calculation")
        sys.exit(1)
