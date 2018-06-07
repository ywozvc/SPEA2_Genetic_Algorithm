import numpy as np
def schaffer_n1(x):
    """
    Description
    ---
    schaffer N1 optimizer test function

    Parameters
    ---
    some

    Return
    ---
    list

    """
    f1 = x**2 # type: float
    f2 = (x-2)**2  # type: float
    return [f1, f2]

