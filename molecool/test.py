import numpy as np

def calculate_square_root(x):
    """
    Calculate the square root of a number.
    
    Parameters
    ----------
    x : float
        The number to calculate the square root of.
    
    Returns
    -------
    root : float
        The square root of x.
    
    Examples
    --------
    >>> calculate_square_root(4)
    2.0
    """
    
    return np.sqrt(x)

print(calculate_square_root(4))

