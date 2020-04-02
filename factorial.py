def factorial(n: int) -> int:
    """ return n! using recursive solution """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
