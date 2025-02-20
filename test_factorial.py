import factorial # type: ignore

def test_factorial():
    """
    Test cases for the factorial function.
    
    Example usage:
    >>> test_factorial()
    """
    assert factorial.factorial(5) == 120
    assert factorial.factorial(0) == 1
    assert factorial.factorial(3) == 6

    # Additional example usage
    factorial.main(5)
    factorial.main(0)
    factorial.main(3)

if __name__ == "__main__":
    import doctest
    doctest.testmod()  # Test the examples in the docstrings
