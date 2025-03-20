def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    lower = 1
    upper = x
    result = (upper + lower) / 2.0

    while abs(result**2 - x) > 0.0001: 
        lower, result = result, (result * result + x) / 2.0

    return result
