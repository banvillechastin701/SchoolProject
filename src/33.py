def sum_of_squares(n):
    """
    Calculate the sum of squares of numbers from 1 to n.
    
    Args:
    - n: An integer representing the upper limit of the range.
    
    Returns:
    - The sum of squares of numbers from 1 to n.
    """
    return (n * (n + 1) * (2 * n + 1)) // 6

# Example usage
result = sum_of_squares(5)
print(result)
