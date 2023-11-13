from flask import session

def simp_function_called():
    """
    Dummy simp function to set simp_called to True.
    """
    session['simp_called'] = True

def subtract_simp(x, y):
    """
    Subtracts y from x and returns the result.
    """
    session['simp_called'] = True
    return x - y

def add_simp(x, y):
    """
    Adds x and y and returns the result.
    """
    session['simp_called'] = True
    return x + y
