from flask import session

def sum_digits(number):
    """
    Sums up the individual digits of a number and returns the result.
    """
    check_simp_called()
    # Convert the number to a string to iterate over its digits
    str_number = str(number)

    # Sum up the digits
    result = sum(int(digit) for digit in str_number)

    return result

def ispal(number):
    """
    Returns True if the number is a palindrome, False otherwise.
    """
    check_simp_called()

    # Convert the number to a string
    str_number = str(number)

    # Check if the string is equal to its reverse
    return str_number == str_number[::-1]

def check_simp_called():
    """
    Checks if a simp function has been called before.
    If not, raises an exception.
    """
    if 'simp_called' not in session or not session['simp_called']:
        raise Exception("A simp function must be called at least once before using comp functions.")
