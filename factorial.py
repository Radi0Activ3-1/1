#Drake Pierce-Demski
#

def factorial(n):
    """
    Calculate the factorial of n using recursion.
    
    Parameters:
    n (int): The number to calculate the factorial for.
    
    Returns:
    int: The factorial of n.
    
    Example:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main(num1):
    """
    Main function to call the factorial function and print the result.
    
    Parameters:
    num1 (int): The number to calculate the factorial for.
    """
    result = factorial(num1)
    print(f"The factorial of {num1} is {result}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()  # Test the examples in the docstrings
